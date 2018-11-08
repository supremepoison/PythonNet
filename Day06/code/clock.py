from multiprocessing import Porcess 

class CloskProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()      #加载父类的init

    def run(self):
        for i in range(5):
            print('Time is {}'.format(time.ctime()))
            time.sleep(self.value)


p =CloskProcess(2)

p.start()
p.join()