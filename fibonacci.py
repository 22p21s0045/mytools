# The class Fibo is used to create a list of fibonacci numbers. 
# 
# The class Fibo is used to select fibonacci numbers from a list of numbers.
class Fibo:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def Create(self,stop):
        global result
        result = []
        start = 0
        second = 1
        for i in range(stop):
            next = start + second
            result.append(next)
            start = second
            second = next
        return result
    def Select(self):
        selectFibo = []
        for i in range(self.start, self.stop):
            if i in result:
                selectFibo.append(i)
        return selectFibo



        
         






        
