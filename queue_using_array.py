class Queue:
  def __init__(self):
    self.__arr = []
    self.__front = 0
    self.__count = 0
  def push(self,ele):
    self.__arr.append(ele)
    self.__count = self.__count + 1
    return
    
  def size(self):
    return self.__count
    
  def is_empty(self):
    if self.size() == 0:
      return True
    return False

  def front(self):
    return self.__arr[self.__front]

  def pop(self):
    if self.is_empty() == True :
      return -1
    else:
      popped_item = self.__arr[self.__front]
      self.__front += 1
      self.__count -= 1
    return popped_item

q = Queue()
q.push(11)
q.push(1111)
q.push(1122)
q.push(11444)
print(q.is_empty())
print(q.size())
while(q.is_empty() is not True):
  print(q.pop())
print(q.is_empty())
  
    
  
