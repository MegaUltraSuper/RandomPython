import time

class Wave(object):

    wave = list()
    
    def __init__(self, length=5):
        self.wave = list()
        for i in range(0,length):
            self.wave.append(' '*i+'\ \n')
        for i in range(0,length):
            self.wave.append(' '*(length-i)+'/ \n')

    def display(self):
        s = ""
        for i in range(0,len(self.wave)):
            s+=self.wave[i]
        print(s)

    def adjust(self):
        self.wave = [self.wave.pop()] + self.wave
    
    def move(self, speed = 1, length = 5):
        """creates a wave with a specified speed 0 to 1
        for a specified time
        """
        if speed>1:
            speed = 1
        if speed<0:
            speed = 0
        start = time.clock()
        while time.clock()-start < length:
            self.display()
            self.adjust()
            time.sleep((1-speed)*.2)
            clear()
        

#sample instance
w1 = Wave(10)

blank = ""
for i in range(45):
    blank+='\n'
    
def clear():
    print(blank)
    
