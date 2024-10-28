class Quees:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enQuee(self,x):
        self.s1.append(x)

    def DeQuee(self):
        if len(self.s1) == 0 and len( self.s2 )==0:
            return -1 
        if len(self.s2) ==0 and len(self.s1)>0:
            while(len(self.s1)):
                temp=self.s1.pop()
                self.s2.append(temp) 
            return self.s2.pop()
        else:
            return self.s2.pop()
q=Quees()
q.enQuee(1)
q.enQuee(2)
q.enQuee(3)
print(q.DeQuee())
print(q.DeQuee())
print(q.DeQuee())