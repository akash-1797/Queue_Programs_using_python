class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.front = None
    self.count = 0

  def push(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node 
      self.tail = new_node
      self.front = new_node
    else:
      self.tail.next = new_node 
      self.tail = new_node
    self.count += 1
    return 
  def pop(self):
    if self.head == None:
      return -1
    else:
      popped_item = self.head.data
      self.head = self.head.next
      self.count -= 1
      self.front = self.front.next
      return popped_item
  def front_at_q(self):
    if self.head == None:
      return -1
    self.front = self.head
    return self.head.data
  def is_empty(self):
    if self.count == 0:
      return True
    else:
      return False
  def get_size(self):
    return self.count

q =   Queue()
q.push(10)
q.push(101)
q.push(102)
q.pop()
print(q.front_at_q())
while(q.is_empty() == False):
  print(q.front_at_q())
  q.pop()
print(q.get_size())
