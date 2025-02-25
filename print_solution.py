from classes.operation import Operation
from classes.task import Task
from classes.service import Service

def print_solution(max_profit: int, max_best_order: list[Task]):
   print(f"Лучшая прибыль: {max_profit}")
   print("Ваполнять операции лучшее в следующем порядке:")
   # for task in max_best_order:
      # print(task.task_name)
      