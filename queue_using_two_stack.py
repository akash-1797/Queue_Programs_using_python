class Queue_using_two_stacks:
  def __init__(self):
    self.s1 = []
    self.s2 = []
  
  def enqueue(self,data):
    while(len(self.s1) != 0):
      x = self.s1.pop()
      self.s2.append(x)
      
    self.s1.append(data)
    
    while(len(self.s2) != 0 ):
      x = self.s2.pop()
      self.s1.append(x)
    return
  
  def dequeue(self):
    if self.is_empty() == True:
      return -1
    else:
      return self.s1.pop()
  
  def front(self):
    if self.size() == 0:
      return -1
    else:
      return self.s1[-1]
  
  def size(self):
    return len(self.s1)


  def is_empty(self):
    if self.size() == 0:
      return True
    else:
      return False

q = Queue_using_two_stacks()
q.enqueue(1)
q.enqueue(11)
q.enqueue(133)
q.enqueue(138491)
print(q.front())
while(q.is_empty() == False):
  print(q.dequeue())
print(q.size())
  
