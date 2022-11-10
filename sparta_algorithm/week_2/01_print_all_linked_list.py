class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# node = Node(3)
# first_node = Node(4)
# node.next = first_node
# # print(node.data)
# # print(node.next.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        #예외 처리
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        # head 노드부터 한 칸씩 이동해서 맨 뒤에 있는 노드까지 이동한다.
        # next 노드에 None이 나온다면 한 칸씩 이동하는 작업은 중지됨.
        while cur.next is not None:
            cur = cur.next
        # 맨 뒤의 노드에 왔다면(cur.next is None이라면) .next로 다음 노드를 추가해준다.
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.print_all()
