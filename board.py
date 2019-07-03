from circularlinkedlist import Node
from circularlinkedlist import CircularLinkedList
from player import Player
from random import randint

class Board:
    def __init__(self):
        """
        __positions: CircularLinkedList
        """
        self.__positions = None
        self.__players = []

    def get_player(self, index):
        return self.__players[index-1]

    def get_positions(self):
        return self.__positions

    def get_scores(self):
        """
        Percorre todos os players e retorna seus pontos
        """
        for i in range(0, len(self.__players)):
            print(f"Player {i+1} has {self.__players[i].get_score()} points")

    def create_board(self, number_of_players, number_of_positions):
        """
        Cria um novo tabuleiro
        """
        self.__positions = CircularLinkedList()
        for i in range(0, number_of_positions):
            self.__positions.insert_front(0)

        for i in range(0, number_of_players):
            self.__players.append(Player(i+1))


    def __len__(self):
        """
        utilizado para retornar a quantidade de posicoes quando len() for cha-
        mado
        """
        return self.__positions.size()

    def roll_the_dice(self):
        """
        Rola o dado.
        """
        return randint(1, 6)

    def print_positions(self):
        """
        Imprime todas as posicoes do tabuleiro e seus respectivos valores
        """
        for i in range(1, self.__len__()+1):
            print(f'[{i}] - {self.__positions.fetch(i)}')
