from operation import Operation
from task import Task
from service import Service
from parser import parse_json_file as parse
import itertools

resource_cost = {
	"programmer" : 8,
	"server": 5,
	"designer": 5,
	"tester": 5,
	"analyst": 2,
	"DevOps":8,
}
#TODO  1) написать функцию которая 
def print_decision(max_profit: int, max_best_order: list[Task]):
   print(f"Лучшая прибыль: {max_profit}")
   print("Ваполнять операции лучшее в следующем порядке:")
   for task in max_best_order:
      print(task.task_name)
      
#функция которая считает прибыль
def profit(service: Service, tasks, Nos: int, time: int):
   income = 0 #прибыль
   expenditure = 0 #расходы
   for task in tasks:
      # print(task.task_name)
      interval = task.Duration()
      time -= interval
      if(time < 0):
         break
      income += Nos * (service.LT * service.AC - (service.CPC / (service.LCR * service.PCR))) * interval
      service.changing_characteristics(task.array)
      
      
      #расходы на задачу(операцию)
      for res in resource_cost:
         expenditure += task.operation.resource_need[res] * resource_cost[res] * interval
   # print("Доход:", income)
   # print("Расходы:", expenditure)
   return income - expenditure

def maximize(service: Service, tasks, Nos: int, time: int):
   max_profit = 0
   max_best_order = []
   # profit(service=service, tasks=tasks, Nos=Nos,time=time)
   permutations = list(itertools.permutations(tasks))
   for perm in permutations:
      prof = profit(service=service, tasks=perm, Nos=Nos,time=time)
      if(prof > max_profit):
         max_profit = prof
         max_best_order = perm
         
   
   print_decision(max_profit= max_profit, max_best_order=max_best_order)

if __name__ == "__main__":
   Nos = 1
   time  = 25
   file_path = "tasks.json"
   tasks = parse(file_path=file_path)
   service = Service(7, 1, 2, 5, 4)
   # print(service)
   maximize(service=service, tasks=tasks, Nos=Nos,time=time)
	