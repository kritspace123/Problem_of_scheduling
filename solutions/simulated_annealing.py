from classes.operation import Operation
from classes.task import Task
from classes.service import Service
from solutions.profit import profit
from print_solution import print_solution

import random
import math
import plotly.graph_objs as go
from plotly.offline import plot

def generate_new_order(order: list[Task]):
   new_state = order[:]
   i = random.randint(0,len(order)-2)
   j = random.randint(0,len(order)-2)
   temp = new_state[i]
   new_state[i] = new_state[j]
   new_state[j] = temp
   return new_state

def simulated_annealing(service: Service, initial_order: list[Task], Nos: int, time: int, initial_temp: int, cooling_rate: float, max_iter: int):
   current_order = initial_order
   current_profit = profit(service=service, tasks=initial_order, Nos=Nos, time=time)
   best_order = current_order
   best_profit = current_profit
   temp = initial_temp
   
   #храним история дохода для построения графика
   profit_history = [current_profit]
   
   for i in range(max_iter):
      new_order = generate_new_order(initial_order)
      new_profit = profit(service=service, tasks=new_order, Nos=Nos, time=time)
      
      # print_solution(new_profit, new_order)
      
      #Проверяем стоит ли переходить в новое состояние
      if new_profit > current_profit or random.random() < math.exp((new_profit - current_profit) / temp):
         current_order = new_order
         current_profit = new_profit
      
      if current_profit > best_profit:
         best_profit = current_profit
         best_order = current_order	
      
      #сохраняем текущую прибыль
      profit_history.append(current_profit)
      
      temp *= cooling_rate
   
   print_solution(max_profit=best_profit, max_best_order=best_order)
   
   #строим график изменение прибыли
   trace = go.Scatter(
		x = list(range(len(profit_history))),
		y = profit_history, 
		mode = 'lines',
		line = dict(color = 'blue')
	)
   
   layout = go.Layout(
		title = "Изменение прибыли в процессе имитации отжига",
		xaxis = dict(title = "Итерации"),
		yaxis = dict(title = "Прибыль"),
	)
   fig = go.Figure(data = [trace], layout = layout)
   plot(fig)