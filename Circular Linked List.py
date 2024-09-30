class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class CLL:

    def __init__(self , last=None):
        self.last = last

    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self , data):
        
        if self.is_empty():
            return None
        
        temp = self.last.next #we need to traverse from first node
        while temp !=self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None
    
    def insert_after(self , temp , data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
            if temp==self.last:#if temp is indicationg only the last node
                self.last= n

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last=None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last=None
            else:
                temp = self.last.next
                while temp.next!= self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item==data:
                        self.delete_first()
                else:
                    temp = self.last.next
                    while temp!= self.last:
                        if temp.next == self.last:
                            if temp.last.item == data:
                                self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next = temp.next.next
                            break

                        temp = temp.next

    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
                    

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp!=self.last:
                print(temp.item , end=" ")
                temp = temp.next
            print(temp.item)

class CLLIterator:

    def __init__(self , start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:#if incase their is node had None in between list
            raise StopIteration
        else:
            self.count=1
        data = self.current.item
        self.current = self.current.next
        

        
        return data
            

myList = CLL()
myList.insert_at_start(29)
myList.insert_at_start(34)
myList.insert_at_last(25)
myList.insert_after(myList.search(34), 78)
myList.insert_at_last(90)
myList.insert_at_last(41)
myList.delete_first()
myList.delete_last()


for x in myList:
    print(x, end=" ")

myList.print_list()
