from classes.operation import Operation
from classes.task import Task
from classes.service import Service
from solutions.profit import profit
from print_solution import print_solution

import random

def local_descent(service: Service, tasks, Nos: int, time: int):
   #рекорд
   max_profit = profit(service=service, tasks=tasks, Nos=Nos, time=time)
   max_best_order = tasks
   cou = 0
   n = len(tasks)
   paste = -1
   while cou < 6:
      tasks1 = max_best_order[:]
      # print_solution(max_profit, tasks1)
      # flag = False
      random_list = random.sample(range(n), random.randint(2, n//2))
      
      pre_max_profiot = 0
      for i in random_list:
         
         if i == paste:
            continue
         
         tasks2 = tasks1[:]
         #Сделал перестановку i-ой и (i+1)-ой задач
         t = tasks2[i]
         tasks2[i] = tasks2[i+1]
         tasks2[i+1] = t
         
         p = profit(service=service, tasks=tasks2, Nos=Nos, time=time)
         if(p > pre_max_profit):
            pre_max_profit = p
            max_best_order = tasks2
            flag = True
            paste = i
            
      
      if(not flag):
         # print(f"Максимальное значение в окрестности:{max(array)}")
         cou += 1
         print(cou)
         break
      
      
   print_solution(max_profit=max_profit, max_best_order= max_best_order)