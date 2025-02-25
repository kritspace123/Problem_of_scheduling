from classes.operation import Operation
from classes.task import Task
from classes.service import Service
from solutions.profit import profit
from print_solution import print_solution

import random

def random_local_descent(service: Service, tasks, Nos: int, time: int):
   #record
   max_profit = profit(service=service, tasks=tasks, Nos=Nos, time=time)
   max_best_order = tasks
   
   cou = 0
   n = len(tasks)
   paste = -1 #будет показывать на какой позиции на прошлом шаге была перестановка
   tasks1 = max_best_order[:]
   while cou < 1000: #критерий остановки мы 5 раз погрузились, но рекорд не улучшили
      
      random_list1 = random.sample(range(n-1), random.randint(2, n//2)) #создаём массив рандомных чисел, который будет использоваться для выбора элементов в подмножество окрестности решения
      
      pre_max_profit = -9999999999999
      pre_best_order = tasks1
      
      for i in random_list1:
         if i == paste:
            continue
         
         tasks2 = tasks1[:]
         #Сделал перестановку i-ой и (i+1)-ой задач
         t = tasks2[i]
         tasks2[i] = tasks2[i+1]
         tasks2[i+1] = t
         
         
         #считаем профит для полученной последовательности
         p = profit(service=service, tasks=tasks2, Nos=Nos, time=time)
         if(p > pre_max_profit):
            pre_max_profit = p
            pre_best_order = tasks2
            paste = i
      
      if(pre_max_profit > max_profit):
         max_profit = pre_max_profit
         max_best_order = pre_best_order
         cou = 0
         continue
      
      #если мы не смогли улучшить рекорд, всёравно переходим в лучшее решение из полученного подмножества окрестности решений
      tasks1 = pre_best_order
      cou += 1
   print_solution(max_profit=max_profit, max_best_order= max_best_order)   