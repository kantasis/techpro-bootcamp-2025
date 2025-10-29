class Node:
   def __init__(self, atad):
      self.data = atad
      self.next = None
    
class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def addElement(self, data):
      node = Node(data)
      node.next = self.head
      self.head = node
      
      if self.head.next is None:
         self.tail = self.head

   def removeHead(self):
      temp = self.head
      self.head = self.head.next
      del temp
      if self.head is None:
         self.tail = None
         

   def length(self):
      counter = 1
      current = self.head
      if current == None:
         return 0

      while current.next != None:
         current = current.next
         counter = counter + 1      
      return counter

   def printEverything(self):
      current = self.head
      while current != None:
         print(current.data)
         current = current.next

   def get(self, n):
      current = self.head
      i=0
      if current == None:
         return "The list is empty"
      while i<n:
         current = current.next
         i = i+1
         if current == None
            return "There is no such"

      return current.data

my_linked_list = LinkedList()

my_linked_list.addElement("George")
my_linked_list.addElement("Afroxilanthi")
my_linked_list.addElement("John")
my_linked_list.addElement("Peter")
my_linked_list.addElement("Paul")

# print(my_linked_list.head.next.next)
# print(my_linked_list.length()) 
# my_linked_list.printEverything()
print(my_linked_list.get(10))



