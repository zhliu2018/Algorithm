class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not previous:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        while current:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False

    def append(self, item):
        current = self.head
        while current.getNext():
            current = current.getNext()
        temp = Node(item)
        current.setNext(temp)

    def index(self, item):
        current = self.head
        idx = 0
        while current:
            if current.getData() == item:
                return idx
            else:
                current = current.getNext()
                idx += 1
        return -1

    def insert(self, pos, item):
        idx = 0
        current = self.head
        temp = Node(item)
        while idx < pos-1:
            current = current.getNext()
            idx += 1
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current.getNext())
            current.setNext(temp)

    def pop(self, pos=None):
        if pos == None:
            pos = self.size() - 1
        i = 0
        previous = None
        current = self.head
        while i < pos:
            previous = current
            current = current.getNext()
            i += 1
        if not previous:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return current

    def reverse(self):
        if (not self.head) or (not self.head.getNext()):
            return
        p = self.head
        q = self.head.getNext()
        self.head.setNext(None)
        while q:
            r = q.getNext()
            q.setNext(p)
            p = q
            q = r
        self.head = p

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.getData()))
            current = current.getNext()
        return ' '.join(items)

if __name__ == '__main__':
    #[54,26,93,17,77,31]
    mylist = LinkList()
    print(mylist.isEmpty())
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print(mylist.size())
    print(mylist.search(93))
    mylist.remove(26)
    print(mylist.size())
    print(mylist)
    mylist.append(55)
    print(mylist)
    print(mylist.index(93))
    mylist.insert(3, 16)
    print(mylist)
    mylist.pop()
    print(mylist)
    mylist.pop(1)
    print(mylist)
    mylist.reverse()
    print(mylist)

