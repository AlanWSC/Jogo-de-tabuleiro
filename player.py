class Player:
    def __init__(self, index):
        """
        Inicia o player na posicao index, inicialmente com 0 pontos

        index: Numero do jogador
        position: posicao do jogador no tabuleiro
        """
        self.__index = index
        self.__score = 0
        self.__position = None

    def add_score(self, points):
        """
        Soma pontos ao player
        """
        if points % 2 == 0:  # Parou em casa Par
            self.__score += 2
        else:
            if self.__score - 1 < 0:
                self.__score = 0
            else:
                self.__score -= 1


    def get_score(self):
        """
        Retorna os pontos do player atual
        """
        return self.__score

    def get_index(self):
        """
        Retorna o index do player
        """
        return self.__index

    def get_position(self):
        """
        Retorna a posicao do jogador no tabuleiro
        """
        return self.__position

    def set_position(self, position):
        """
        Define uma nova posicao para o jogador no tabuleiro
        """
        self.__position = position
    def __str__(self):
        """
        Metodo chamado quando um objeto precisa ser impresso
        """
        if self.__index:
            return 'Player ' + str(self.__index)

    #def __repr__(self):
    #    return self.__str__()
