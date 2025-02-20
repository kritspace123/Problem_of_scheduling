from classes.operation import Operation
from classes.task import Task
from classes.service import Service

resource_cost = {
	"programmer" : 8,
	"server": 5,
	"designer": 5,
	"tester": 5,
	"analyst": 2,
	"DevOps":8,
}


def changing_characteristics(array: list[int], task_array: list[int]) -> list[int]:
   for i in range(len(array)):
      array[i] += task_array[i]
   return array

#функция которая считает прибыль
def profit(service: Service, tasks, Nos: int, time: int):
   array = service.get_array()
   income = 0 #прибыль
   expenditure = 0 #расходы
   for task in tasks:
      # print(task.task_name)
      interval = task.Duration()
      time -= interval
      if(time < 0):
         break
      income += Nos * (array[0] * array[1] - (array[2] / (array[3] * array[4]))) * interval
      array = changing_characteristics(array=array, task_array=task.array)
      
      
      #расходы на задачу(операцию)
      for res in resource_cost:
         expenditure += task.operation.resource_need[res] * resource_cost[res] * interval
   # print("Доход:", income)
   # print("Расходы:", expenditure)
   return income - expenditure