from words_generator import *
from menus import *

def main():
    stats = open('statistics.txt', 'r')
    game_number = int(len(stats.readlines())/4 + 1)
    stats.close()
    tries = 0
    word_and_context = generate_word()
    word_to_guess = list(word_and_context[0].upper())
    context = word_and_context[1].upper()
    context_bool = False
    guessed = []
    word_now = create_word_sep(word_to_guess)
    valid_state = False
    """The 'left_game' variable wil not only decide if the game starts, but also will print the menu, calling the menu functions"""
    left_game = menu_selection(main_menu())
    
    if not left_game:
        os.system('cls')
        while not valid_state:
            """Error treatment for the user input"""
            print("Vai querer a dica do contexto da palavra?\n Digite S para sim ou N para nao")
            context_input = str(input())
            os.system('cls')
            if context_input=="S" or context_input=="s":
                context_bool = True
                valid_state = True
            elif context_input=="N" or context_input=="n":
                valid_state = True
            else:
                print("Digite um caractere valido, por favor!\n")
                
        while tries<len(STATES)-1 and '_' in word_now:
            current_state = STATES[tries]
            correct_answer = False
            already_tried = True
            print(current_state)
            print("      ", end='')
            for i in range(len(word_now)):
                print(word_now[i], end='')
            print("\n\n")
            
            if context_bool:
                """Decides if the program will print the context in which the word is inserted corresponding to the user's choice"""
                print(f"O contexto em que a palavra esta inserida e: {context}, e voce ainda tem {len(STATES)-tries-1} chances para acertar\n")
            else:
                print(f"Voce ainda tem {len(STATES)-tries-1} chances para acertar\n")

            while already_tried:
                """Error treatment for the user's guess, checking if it is a letter and if it wasn't already tried"""
                guess = str(input("E entao... qual seu chute?  \n")).upper()
                if not guess.isalpha():
                    print("Insira um caractere valido, por favor!")
                else:
                    if(guess in guessed):
                        print("Essa voce ja tentou! Tenta outra!\n")
                    else:
                        guessed.append(guess)
                        already_tried = False
                        
            for i in range(len(word_to_guess)):
                """Checking for each letter in the answer if it corresponds to the user's guess, updating the already guessed word's state"""
                if guess == word_to_guess[i]:
                    word_now[i] = guess
                    correct_answer = True
            os.system('cls')
            if not correct_answer:
                tries+=1
                print(f"\nPoxa, a letra '{guess}' nao estava la...\n")
            else:
                print(f"\nBoa, realmente a letra '{guess}' estava la!\n")
        
        """Organizing the statistics on the save file"""
        victory = False
        victory_msg = 'Derrota'
        if '_' not in word_now:
            victory = True
            victory_msg = 'Vitoria'
        stats = open('statistics.txt', 'a')
        stats.write(f'Jogo {game_number}\n{victory_msg}\nErrou {tries} vezes\nA palavra foi: {word_and_context[0]}\n')
        stats.close()
        
        """Printing the final state the user have achieved"""
        current_state = STATES[tries]
        print(current_state)
        print("      ", end='')
        for i in range(len(word_now)):
            print(word_now[i], end='')
        print("\n\n")
        
        if victory:
            if tries==1:
                print(f'Parabens! Voce chegou na resposta errando {tries} vez!')
            elif tries>1:
                print(f'Parabens! Voce chegou na resposta errando {tries} vezes!')
            else:
                print(f'Parabens! Voce chegou na resposta sem errar uma sequer!')
        else:
            print(f'Voce perdeu... f')
    else:
        print("Obrigado por jogar, tchau!")

if(__name__ == '__main__'):
    main()