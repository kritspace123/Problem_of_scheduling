import time

from classes.operation import Operation
from classes.task import Task
from classes.service import Service
from parser import parse_json_file as parse
from solutions.profit import profit

#Solution
from solutions.nFAC_solution import maximize
from solutions.local_descent import local_descent
from solutions.randomnoe import random_local_descent
from solutions.simulated_annealing import simulated_annealing


resource_cost = {
	"programmer" : 8,
	"server": 5,
	"designer": 5,
	"tester": 5,
	"analyst": 2,
	"DevOps":8,
}


if __name__ == "__main__":
   start_time = time.time()
   Nos = 1
   time_1 = 25
   file_path = "tasks.json"
   tasks = parse(file_path=file_path)
   service = Service(7, 1, 2, 5, 4)
   
   # print(profit(service=service, tasks=tasks, Nos=Nos, time=25))
   
   
   #Обычный брутфорс: O(n!)
   # maximize(service=service, tasks=tasks, Nos=Nos,time=time_1)
   
   #Локальный спуск: O(..)
   # local_descent(service=service, tasks=tasks, Nos=Nos,time=time_1)
   
   #Рандомизированный локальный спуск
   # random_local_descent(service=service, tasks=tasks, Nos=Nos,time=time_1)
   
   #Имитация отжига SA
   initial_temp = 4000 #начальная температура
   initial_rate = 0.995 # коэффициент охлаждения
   max_iter = 10000 #максимальное количество итераций
   simulated_annealing(service=service, initial_order=tasks, Nos= Nos, time= time_1, initial_temp=initial_temp, cooling_rate=initial_rate, max_iter=max_iter)
   
   end_time = time.time()
   print(f"Время выполнение: {end_time - start_time}")
	