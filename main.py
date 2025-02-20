from classes.operation import Operation
from classes.task import Task
from classes.service import Service
from parser import parse_json_file as parse

#Solution
from solutions.nFAC_solution import maximize

resource_cost = {
	"programmer" : 8,
	"server": 5,
	"designer": 5,
	"tester": 5,
	"analyst": 2,
	"DevOps":8,
}


if __name__ == "__main__":
   Nos = 1
   time  = 25
   file_path = "tasks.json"
   tasks = parse(file_path=file_path)
   service = Service(7, 1, 2, 5, 4)
   # print(service)
   maximize(service=service, tasks=tasks, Nos=Nos,time=time)
   # tasks2 = [tasks[2], tasks[1], tasks[0]]
   # print(profit(service=service, tasks=tasks2, Nos=Nos, time=25))
   
	