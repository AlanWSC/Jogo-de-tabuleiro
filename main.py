from board import Board
import time
import os


if __name__ == '__main__':
    board = Board()

    # Recuperando informações sobre a partida
    board_size = int(input('Informe a quantidade de posicoes:'))
    number_of_players = int(input('Informe a quantidade de players:'))

    # Criação do tabuleiro
    board.create_board(number_of_players, board_size)

    winner = None
    max_score = 10 # Condicao de vitoria
    while winner == None:
        # O for simula uma rodada de jogadas
        for player in range(1, number_of_players+1):
            print("======== Jogo de Tabuleiro +2-1 ========")
            print('----------------Tabuleiro---------------')
            board.print_positions()
            print('---------------Pontos------------------')
            board.get_scores()
            print('--------------------------------------')
            print('')
            print(f'Jogador {player} rolou o dado')
            # time.sleep(2)
            dice_result = board.roll_the_dice()
            print(f'Resultado: {dice_result}')

            # Criou uma variavel para armazenar a casa em
            # que o jogador caiu
            casa_resultante = board.get_positions().move(board.get_player(player), dice_result, board_size)

            # adiciono uma potuacao correspondente aquela casa
            board.get_player(player).add_score(casa_resultante)

            if board.get_player(player).get_score() >= max_score:
                winner = board
                print('Jogador %d é o vencedor!!!'%player)



            q = input('Pressione Enter para continuar!')

            #Limpa a tela a cada rodada
            os.system('cls' if os.name == 'nt' else 'clear')

