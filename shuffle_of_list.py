class employee:

    def __init__(self, name, salary):
       self.name = name
       self.salary = salary

worker_1 = employee("hari", 6000)
worker_2 = employee("fazil", 5000)
worker_3 = employee("harinath", 600)
worker_4 = employee("sai", 9000)


list_of_workers = [worker_1, worker_2, worker_3, worker_4]

try:
 shuffled_list = random.shuffle(list_of_workers)  #shuffle return None as error in assignment operation
 for i in shuffled_list:
  print(i.name, i.salary)
     
except Exception:
    pass

finally:
    shuffled_list = random.sample(list_of_workers, len(list_of_workers)) #sample will not repeat the list
    for i in shuffled_list:
        print(i.name, i.salary)
