from classes.operation import Operation
from classes.task import Task
from classes.service import Service
from solutions.profit import profit
from print_solution import print_solution

def local_descent(service: Service, tasks, Nos: int, time: int):
   max_profit = profit(service=service, tasks=tasks, Nos=Nos, time=time)
   max_best_order = tasks
   cou = 1
   while True:
      tasks1 = max_best_order[:]
      # print_solution(max_profit, tasks1)
      flag = False
      array = []
      for i in range(len(tasks)-1):
         
         
         tasks2 = tasks1[:]
         #Сделал перестановку i-ой и (i+1)-ой задач
         t = tasks2[i]
         tasks2[i] = tasks2[i+1]
         tasks2[i+1] = t
         
         p = profit(service=service, tasks=tasks2, Nos=Nos, time=time)
         if(p > max_profit):
            max_profit = p
            max_best_order = tasks2
            flag = True
      
      if(not flag):
         # print(f"Максимальное значение в окрестности:{max(array)}")
         print(cou)
         break
      cou += 1
      
   print_solution(max_profit=max_profit, max_best_order= max_best_order)