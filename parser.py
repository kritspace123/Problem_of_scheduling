from task import Task
from operation import Operation

import json
from dataclasses import dataclass
from typing import List


def parse_resource_need(resource_need: dict) -> dict:
   resource = {}
   resource["programmer"] = resource_need["programmer"]
   resource["server"] = resource_need["server"]
   resource["designer"] = resource_need["designer"]
   resource["tester"] = resource_need["tester"]
   resource["analyst"] = resource_need["analyst"]
   resource["DevOps"] = resource_need["DevOps"]
   return(resource)

def parse_operation(operation_data: dict):
   # operations = []
   for operation in operation_data:
      #собираем данные по каждой операции и создаём обьект класса Operation
      operation_id = operation["operation_id"]
      duration = operation["duration"]
      resource_need = parse_resource_need(operation["resource_need"])
      op = Operation(id=operation_id, duration=duration, resource_need=resource_need)
      return op
      # operations.append(op)
   # return(operations)


def parse_task(task_data: dict) -> List[Task]:
   tasks = []
   for task in task_data:
      #собираем данные по каждой задаче и создаём обьект класса Task
      task_id = task["task_id"]
      task_name = task["task_name"]
      operation = parse_operation(task["operations"])
      array = task["array"]
      taska = Task(id = task_id, task_name=task_name, operation = operation, array=array)
      tasks.append(taska)
   return tasks
      

def parse_json_file(file_path: str) -> List[Task]:
   # Чтение данных из JSON файла
   with open(file_path, 'r', encoding='utf-8') as file:
      data =json.load(file) # Загружаем данные из JSON
      return parse_task(data["tasks"])
      # return [task for task in parse_task(data["tasks"])]





# def parse_resource_need(resource_data: dict) -> dict:
# 	return {
# 		"programmer" : resource_data['programmer'],
# 		"server" : resource_data['server'],
# 		"designer" : resource_data['designer'],
# 		"tester" : resource_data['tester'],
# 		"analyst" : resource_data['analyst'],
# 		"DevOps" : resource_data['DevOps']
# }



# def parse_operation(operation_data: dict) -> Operation:
# 	resource_need = parse_resource_need(operation_data['resource_need'])
# 	return Operation(operation_data['operation_id'], operation_data['duration'], resource_need)


# def parse_task(task_data: dict) -> Task:
# 	operations = parse_operation(task_data['operations'])
# 	return Task(task_data['task_id'], task_data['task_name'], operations, task_data['array'])
# 	# return Task(
# 	# 	id=task_data['task_id'],
# 	# 	task_name=task_data['task_name'],
# 	# 	operations=operations,
# 	# 	array=task_data['array']
# 	# )

# def parse_json_file(file_path: str) -> List[Task]:
# 	# Чтение данных из JSON файла
# 	with open(file_path, 'r', encoding='utf-8') as file:
# 		data = json.load(file)  # Загружаем данные из JSON
#    #  Преобразуем данные в объекты
# 	return [parse_task(task) for task in data['tasks']]



# Пример использования
# file_path = 'tasks.json'  # Путь к вашему JSON файлу
# tasks = parse_json_file(file_path)

# # Проверим результат
# for task in tasks:
# 	print(task)
