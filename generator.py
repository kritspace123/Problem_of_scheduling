import json
import random

def generate_task_json(num_tasks):
   tasks = []
   for i in range(1, num_tasks + 1):
      task = {
         "task_id": i,
         "task_name": f"Задача {i}",
         "operations": [],
         "array": [random.randint(1, 5) for _ in range(5)]  # Генерация массива случайных чисел
      }
      num_operations = 2
      #   num_operations = random.randint(1, 3)  # Генерация случайного количества операций от 1 до 3 для каждой задачи
      
      for j in range(1, num_operations):
         operation = {
            "operation_id": j,
            "duration": random.randint(1, 10),  # Генерация случайной длительности операции от 1 до 10
            "resource_need": {
					"programmer": random.randint(1, 3),  # Генерация случайного числа от 1 до 3
					"server": random.randint(1, 3),
					"designer": random.randint(1, 2),
					"tester": random.randint(1, 2),
					"analyst": random.randint(1, 2),
					"DevOps": random.randint(1, 2)
            },
         }
         task["operations"].append(operation)
         

      tasks.append(task)
   return {"tasks": tasks}

def save_json_to_file(filename, num_tasks):
	# Генерация данных
	data = generate_task_json(num_tasks)
	
	# Сохранение данных в файл
	with open(filename, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)
	print(f"Данные успешно сохранены в файл {filename}")

def save_json_to_file(filename, num_tasks):
	# Генерация данных
	data = generate_task_json(num_tasks)
	
	# Сохранение данных в файл
	with open(filename, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)
	print(f"Данные успешно сохранены в файл {filename}")

def generate_resources_json():
	resources = {
		"programmer": [random.randint(1, 8), random.randint(1, 10)],
		"server": [random.randint(1, 8), random.randint(1, 10)],
		"designer": [random.randint(1, 8), random.randint(1, 10)],
		"tester": [random.randint(1, 8), random.randint(1, 10)],
		"analyst": [random.randint(1, 8), random.randint(1, 10)],
		"DevOps": [random.randint(1, 8), random.randint(1, 10)]
	}
	return {"recources": resources}

def save_resources_json_to_file(filename):
	# Генерация данных о ресурсах
	data = generate_resources_json()
	
	# Сохранение данных в файл
	with open(filename, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)
	print(f"Данные о ресурсах успешно сохранены в файл {filename}")


save_json_to_file("tasks.json", 300)  # Сохранение данных о задачах в файл "tasks.json"
save_resources_json_to_file("resources.json")  # Сохранение данных о ресурсах в файл "resources.json"