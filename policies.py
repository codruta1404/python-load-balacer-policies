import random
import multiprocessing
from machine import Machine
from machine import CPU_Machine

class Scheduler:
    def __init__(self):
        self.workers_info_list = [{"region":"asia", "id":"0", "cost":2},
                                  {"region":"asia", "id":"1", "cost":2},
                                  {"region":"emea", "id":"0", "cost":2},
                                  {"region":"us", "id":"0", "cost":1},
                                  {"region":"us", "id":"1", "cost":1}]
        self.workers_list = []

    def random_lb(self, nr_req):
        count = nr_req
    
        for i, worker in enumerate(self.workers_info_list):
            if count != 0:
                if i == len(self.workers_info_list) - 1:
                    machine = Machine(worker["region"], worker["id"], count)
                    self.workers_list.append(machine)
                    break
                r = random.randint(1, count)
                machine = Machine(worker["region"], worker["id"], r)
                count = count - r
                self.workers_list.append(machine)

        self.run_workers()
        self.join_workers()

        avrg_time = 0
        for worker in self.workers_list:
            avrg_time = avrg_time + worker.resp_time

        avrg_time = avrg_time / len(self.workers_list)
        print('Average time:', avrg_time)

        self.workers_list = []

    def round_robin_lb(self, nr_req):
        req_per_machine = int(nr_req / len(self.workers_info_list))
        rest = nr_req % len(self.workers_info_list)
        
        for worker in self.workers_info_list:
            reqs = req_per_machine
            if rest > 0:
                reqs = reqs + 1
                rest = rest - 1 
            machine = Machine(worker["region"], worker["id"], reqs)
            self.workers_list.append(machine)

        self.run_workers()
        self.join_workers()

        avrg_time = 0
        for worker in self.workers_list:
            avrg_time = avrg_time + worker.resp_time

        avrg_time = avrg_time / len(self.workers_list)
        print('Average time:', avrg_time)

        self.workers_list = []

    def second_random_lb(self, nr_req):
        req_per_machine = int(nr_req / len(self.workers_info_list))
        rest = nr_req % len(self.workers_info_list)
        count = req_per_machine
        remain = 0
        r = 0
        rest_req = nr_req

        for i, worker in enumerate(self.workers_info_list):
            if rest_req != 0:
                if i == len(self.workers_info_list) - 1:
                    machine = Machine(worker["region"], worker["id"], rest_req)
                    self.workers_list.append(machine)
                    break
                r = random.randint(1, count)
                remain = count - r
                count = req_per_machine + remain
                if rest > 0:
                    r = r + 1
                    rest = rest - 1     
                machine = Machine(worker["region"], worker["id"], r)
                rest_req = rest_req - r
                self.workers_list.append(machine)

        self.run_workers()
        self.join_workers()

        avrg_time = 0
        for worker in self.workers_list:
            avrg_time = avrg_time + worker.resp_time

        avrg_time = avrg_time / len(self.workers_list)
        print('Average time:', avrg_time)

        self.workers_list = []

    def cpu_work_lb(self, nr_req):
        num_cpus = multiprocessing.cpu_count()
        reqs = int(nr_req / num_cpus)
        rest = nr_req % num_cpus

        for i in range(num_cpus):
            if i == 0:
                cpu_machine = CPU_Machine(reqs + rest)
            else:
                cpu_machine = CPU_Machine(reqs)
            self.workers_list.append(cpu_machine)

        self.run_workers()
        self.join_workers()

        avrg_time = 0
        for worker in self.workers_list:
            avrg_time = avrg_time + worker.resp_time_CPU

        avrg_time = avrg_time / len(self.workers_list)
        print('Average time:', avrg_time)

        self.workers_list = []
            
    def response_time_lb(self, nr_req): 
        total_cost = 0
        rest = 0

        for worker in self.workers_info_list:
            total_cost = total_cost + worker["cost"]

        for worker in self.workers_info_list:
            raport = (worker["cost"]) / total_cost
            reqs = int(raport * nr_req)
            machine = Machine(worker["region"], worker["id"], reqs)
            self.workers_list.append(machine)

        self.run_workers()
        self.join_workers()

        avrg_time = 0
        for worker in self.workers_list:
            avrg_time = avrg_time + worker.resp_time

        avrg_time = avrg_time / len(self.workers_list)
        print('Average time:', avrg_time)

        self.workers_list = []

    def run_workers(self):
        for worker in self.workers_list:
            worker.start()
    
    def join_workers(self):
        for worker in self.workers_list:
            worker.join()
            






        
        



