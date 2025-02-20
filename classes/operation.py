class Operation:
   def __init__(self, id: int , duration : int, resource_need: dict):
      self.id = id
      self.duration = duration
      self.resource_need = resource_need
	
   def __str__(self):
      return f"""
	"operation_id": {self.id},
	"duration": {self.duration}",
	"resource_need": 
		"programmer": {self.resource_need["programmer"]},
		"server": {self.resource_need["server"]},
		"designer": {self.resource_need["designer"]},
		"tester": {self.resource_need["tester"]},
		"analyst": {self.resource_need["analyst"]},
		"DevOps": {self.resource_need["DevOps"]}
"""