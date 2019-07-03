from enum import Enum

class NodeConstants(Enum):
    FRONT_NODE = 1


class Node:
    """
    Cria um nodo que pode ser armazenado na lista.

    Parametros
    ----------
    element: qualquer tipo
        Qualquer elemento que deseje-se armazenar
    next_node: Node
        Referencia para o proximo nodo
    node_score: int, default = 0
        Define quando o nodo esta valendo atualmente
    """
    def __init__(self, element=None, next_node=None, node_score=0):
        """
        element: qualquer elemento que deseje ser armazenado
        next_node: referencia para o proximo nodo
        self.node_score: pontuacao atual do nodo
        """
        self.element = element
        self.next_node = next_node
        self.node_score = 0

    def change_element(self, element):
        self.element = element



class CircularLinkedList:
    """
    Cria uma lista circular encadeada

    Parametros
    ----------
    head: Node
    Cabeca da lista
    """
    def __init__(self):
        self.head = Node(NodeConstants.FRONT_NODE)

        self.head.next_node = self.head

    def size(self):
        """
        Retorna o tamanho da lista
        """
        count = 0
        current = self.head.next_node

        while current != self.head:
            count += 1
            current = current.next_node

        return count

    def insert_front(self, data):
        """
        Insere no inicio da lista
        """
        node = Node(data, self.head.next_node)
        self.head.next_node = node

    def insert_last(self, data):
        """Insere no final da lista."""
        current_node = self.head.next_node

        while current_node.next_node != self.head:
            current_node = current_node.next_node

        node = Node(data, current_node.next_node)
        current_node.next_node = node

    def insert(self, data, index):
        """Insere o player na posicao index."""
        if index == 1:
            self.insert_front(data)
        elif index == self.size() + 1: 
            self.insert_last(data)
        else:
            if 1 < index <= self.size():
                current_node = self.head.next_node
                current_pos = 1

                while current_pos < index - 1:
                    current_pos += 1
                    current_node = current_node.next_node

                node = Node(data, current_node.next_node)
                current_node.next_node = node
            else:
                raise IndexError

    def fix_position(self, data, index, board_size):
        """Determina a posicao correta que o player será inserido."""
        position_player = data.get_position()
        if position_player != None:
            if (position_player + index) > board_size:
                index = (position_player - board_size) + index
            else:
                index = position_player + index
            self.remove(position_player)
            self.insert(0, position_player)

        while self.fetch(index) != 0:
            index = self.get_next_index(index)
        return index


    def move(self, data, index, board_size):
        """Movo o player de posicao no tabuleiro."""
        if data.get_position != None:
            index = self.fix_position(data, index, board_size)

        if index == 1:
            self.remove_first()
            self.insert_front(data)
            data.set_position(index)
            self.node_score = 1
            return self.node_score
        elif index == self.size():
            self.remove_last()
            self.insert_last(data)
            data.set_position(index)
            self.node_score = index + 1
            return self.node_score
        else:
            if 1 < index < self.size():
                self.remove(index)
                self.insert(data, index)
                data.set_position(index)
                self.node_score = index + 1
                return self.node_score
            else:
                raise IndexError

    def remove_first(self):
        """Remove o primeiro nodo."""
        self.head.next_node = self.head.next_node.next_node

    def remove_last(self):
        """Remove o ultimo nodo"""
        current_node = self.head.next_node

        while current_node.next_node.next_node != self.head:
            current_node = current_node.next_node

        current_node.next_node = self.head

    def remove(self, index):
        """Remove um nodo na posicao index."""
        if index == 1:
            """
            Se for primeiro, chama uma funcao existente
            que remove o primeiro
            """
            self.remove_first()
        elif index == self.size():
            """
            Se for o ultimo, chama uma funcao existente
            que remove o ultimo
            """
            self.remove_last()
        else:
            if 1 < index < self.size():
                current_node = self.head.next_node
                current_pos = 1

                while current_pos < index - 1:
                    current_node = current_node.next_node
                    current_pos += 1

                current_node.next_node = current_node.next_node.next_node
            else:
                raise IndexError

    def fetch(self, index):
        """Retorna o elemento na posição index."""
        if 1 <= index <=self.size():
            current_node = self.head.next_node
            current_pos = 1

            while current_pos < index:
                current_node = current_node.next_node
                current_pos += 1

            return current_node.element
        else:
            raise IndexError

    def get_next_index(self, index):
        """Retorna o proximo index.

        caso o index recebido seja o ultimo, retorna 0 (primeiro)
        """
        if index == self.size():
            return 1
        else:
            return index + 1
