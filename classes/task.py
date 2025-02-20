from classes.operation import Operation
class Task:
   def __init__(self, id: int, task_name: str, operation: Operation, array):
      self.id = id
      self.task_name = task_name
      self.operation = operation
      self.array = array
      
   def Duration(self):
      return self.operation.duration
   
   def __str__(self):
      return f"""
   
"task_id": {self.id},
"task_name": {self.task_name}
"operations": {self.operation}
"array": {self.array}

"""