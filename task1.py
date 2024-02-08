class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next
        print()

    def len_list(self):
        len = 0
        current = self.head
        while current:
            len += 1
            current = current.next
        return len

    def reverse_list(self):
        prev = self.head
        current = prev.next
        prev.next = None
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev
        

    def merge_sort(self):
        if self.len_list() <= 1:
            return self
        mid = self.len_list()//2
        left_list = LinkedList()
        current = self.head
        for i in range(mid):
            left_list.insert_at_end(current.data)
            current = current.next
        right_list = LinkedList()
        right_list.head = current
        left_list = left_list.merge_sort()
        right_list = right_list.merge_sort()
        self.head = left_list.merge(right_list).head
        return self
        

    def merge(self, list2):
        merged = LinkedList()
        first = self.head
        second = list2.head

        while first and second:
            if first.data < second.data:
                merged.insert_at_end(first.data)
                first = first.next
            else:
                merged.insert_at_end(second.data)
                second = second.next

        while first:
            merged.insert_at_end(first.data)
            first = first.next
        
        while second:
            merged.insert_at_end(second.data)
            second = second.next
        
        return merged




if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Linked list 1:")
    llist.print_list()

    llist.reverse_list()
    print("Reversed linked list 1:")
    llist.print_list()

    llist.merge_sort()
    print('Sorted linked list 1 with merge sort:')
    llist.print_list()

    llist2 = LinkedList()

    # Вставляємо вузли в початок
    llist2.insert_at_beginning(7)
    llist2.insert_at_beginning(3)
    llist2.insert_at_beginning(1)
    llist2.insert_at_beginning(9)
    llist2.insert_at_beginning(21)
    llist2.insert_at_beginning(15)
    llist2.insert_at_beginning(8)

    # Друк зв'язного списку
    print("Linked list 2:")
    llist2.print_list()

    llist2.reverse_list()
    print("Reversed linked list 2:")
    llist2.print_list()

    llist2.merge_sort()
    print('Sorted linked list 2 with merge sort:')
    llist2.print_list()

    merged = llist.merge(llist2)

    print("Merged sorted linked list 1 with sorted linked list 2:")
    merged.print_list()
   
