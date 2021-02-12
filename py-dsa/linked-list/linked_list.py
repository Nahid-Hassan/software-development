class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    @property
    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove(self, index):
        if index < 0 or index >= self.get_length:
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def display(self):
        if self.head is None:
            print("My linked list is empty.")
            return

        itr = self.head
        llstr = str()

        while itr:
            llstr += str(itr.data) + ', '
            itr = itr.next

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['mango', 'banana', 'orange'])
    ll.display()
    print(ll.get_length)
    ll.remove(4)
    ll.display()
    print(ll.get_length)
