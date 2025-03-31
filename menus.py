import os

def menu_selection(selection:str) -> bool:
    """Selects the menu based on the string returned by the function main_menu()"""
    left_game = False
    left_menu = False
    while not left_menu:
        os.system('cls')
        match selection:
            case 'Q':
                left_menu = True
                left_game = True
            case 'S':
                stats = open('statistics.txt', 'r')
                lines = stats.readlines()
                if len(lines) == 0:
                    print("Nao ha estatisticas suficientes de seus jogos para ler, jogue ao menos uma vez!\n")
                else: 
                    for line in lines:
                        print(line)
                valid_decision = False
                print("Gostaria de retornar ao menu?\nTecle 'S' para sim ou 'N' para nao")
                menu_decision = str(input()).upper()
                while not valid_decision:
                    if menu_decision not in ['S','N']:
                        print("Ou e sim, ou nao cara! Tecle um caractere correspondente!")
                    else:
                        valid_decision = True
                if menu_decision == 'S':
                    selection = main_menu()
                else:
                    print("Ok, saindo do jogo, entao!")
                    left_game = True
                stats.close()
                left_menu = True
            case 'E':
                left_menu = True
    return left_game

def main_menu() -> str:
    """Standard function to begin the program and get the user's choice for the menu selection"""
    valid_input = False
    possible_inputs = ['Q', 'S', 'E']
    print(116*"-"+"\n")
    print("Seja bem vindo(a) ao jogo da forca!\nVoce tera 6 chances de acertar a palavra escolhida aleatoriamente pelo programa!\n")
    print("Primeiro, escolha uma das seguintes opcoes, escrevendo a letra correspondente:\n")
    while not valid_input:
        print("'E' para jogar\n'S' para ver suas estatisticas\n'Q' para sair")
        selection = str(input())
        if not selection.isalpha:
            print("Caractere invalido, insira uma das letras especificadas!")
        else:
            selection = selection.upper()
            if selection not in possible_inputs:
                print("Essa letra nao esta dentre as possiveis para a selecao do menu! Tecle novamente!")
            else:
                valid_input = True
    return selection