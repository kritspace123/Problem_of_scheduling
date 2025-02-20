from classes.operation import Operation
from classes.task import Task
from classes.service import Service
from profit import profit
from print_solution import print_solution
import itertools

def maximize(service: Service, tasks, Nos: int, time: int):
   max_profit = -10000
   max_best_order = []
   # print(profit(service=service, tasks=tasks, Nos=Nos,time=time))
   permutations = list(itertools.permutations(tasks))
   for perm in permutations:
      prof = profit(service=service, tasks=perm, Nos=Nos,time=time)
      if(prof > max_profit):
         max_profit = prof
         max_best_order = perm
         
   
   print_solution(max_profit= max_profit, max_best_order=max_best_order)