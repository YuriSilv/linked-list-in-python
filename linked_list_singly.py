class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_List():
    def __init__(self):
        self.head = node() 
        self.node_count = 0

    def append_node(self, data):
        new_node = node(data)

        if (self.head.next == None):
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.node_count += 1

    def display(self):
        elements = []
        current_node = self.head

        while (current_node.next != None):
            current_node = current_node.next
            elements.append(current_node.data)

        if (len(elements) == 0):
            print('Lista vazia')
        else:
            for pos,data in enumerate(elements):
                if (pos == len(elements)-1):
                    print(f'{data}', end='')
                    break

                print(f'{data} -> ', end='')

    def get_node(self, index):
        if (index > self.node_count or index < 0):
            print('Erro: index inválido')
            return None
        
        cur_index = 0
        cur_node = self.head

        while True:
            cur_node = cur_node.next
            if (cur_index == index):
                return cur_node.data
            cur_index += 1

    def delete_node(self, index):
        if (index > self.node_count):
            print('Erro: index inválido')
            return None

        cur_index = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if (cur_index == index):
                last_node.next = cur_node.next
                del cur_node
                self.node_count -= 1
                return
            cur_index += 1