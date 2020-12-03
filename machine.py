import threading
import requests

class Machine(threading.Thread):
    def __init__(self, region, id, reqs):
        threading.Thread.__init__(self)
        self.region = region
        self.id = id
        self.reqs = reqs
        self.resp_time = 0
      
    def run(self):
        for req in range(self.reqs):
            r = requests.get('http://0.0.0.0:5000/work/' + self.region + '/' + self.id)
            self.resp_time = self.resp_time + r.json()['response_time']
        self.resp_time = self.resp_time / self.reqs
        
 
class CPU_Machine(threading.Thread):
    def __init__(self, reqs):
        threading.Thread.__init__(self)
        self.reqs = reqs
        self.resp_time_CPU = 0

    def run(self):
        for req in range(self.reqs):
            r = requests.get('http://0.0.0.0:5000/work')
            self.resp_time_CPU = self.resp_time_CPU + r.json()['response_time']
        self.resp_time_CPU = self.resp_time_CPU / self.reqs
