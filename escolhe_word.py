import random
import json

def choose_random_word(dictionary):
    if len(dictionary) > 0:
        while True:
            word = random.choice(list(dictionary.keys()))
            if '.' not in word and len(word) <= 8 and len(word) >= 2 and ' ' not in word:
                return word
    else:
        raise ValueError("O dicionário está vazio.")

def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def is_valid_word(guess, word):
    return guess == word

def get_definition(word, dictionary):
    return dictionary[word]

def load_dictionary(file_path):
    with open(file_path, "r") as file:
        dictionary = json.load(file)
    return dictionary

def get_hint(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    hint = ['_'] * len(word)
    for i, char in enumerate(word):
        if char in vowels:
            hint[i] = char
    return ''.join(hint)

def play_anagram_game(dictionary):
    word = choose_random_word(dictionary)
    shuffled_word = shuffle_word(word)

    print("***********************************")
    print("*   Bem-vindo ao Jogo de Anagramas   *")
    print("***********************************\n")

    print("Você tem 3 chances para adivinhar a palavra abaixo.")
    print("Tente desembaralhar as letras para formar uma palavra válida.\n")
    print("Palavra embaralhada:", shuffled_word)

    hint_given = False
    guesses = 0

    while guesses < 3:
        print("\nChances restantes:", 3 - guesses)
        guess = input("Qual é a palavra desembaralhada? ").strip().lower()

        if guess == 'dica':
            if not hint_given:
                hint_given = True
                hint = get_hint(word)
                print("\nDica: A palavra contém as seguintes vogais:", hint)
            else:
                print("Você já recebeu uma dica. Tente adivinhar a palavra.")
            continue

        if guess == 'definição':
            definition = get_definition(word, dictionary)
            print("\nDefinição:", definition)
            continue

        if is_valid_word(guess, word):
            print("\nParabéns! Você acertou a palavra!")
            break

        print("Desculpe, essa não é a palavra correta.")
        guesses += 1

    if guesses == 3:
        print("\nSuas chances acabaram. A palavra correta era:", word)

        if not hint_given:
            hint = get_hint(word)
            if hint:
                print("Dica: A palavra contém as seguintes vogais:", hint)

    play_again = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if play_again == 's':
        print("\n")
        play_anagram_game(dictionary)
    else:
        print("\nObrigado por jogar!")

# Load the dictionary from JSON file
dictionary = load_dictionary("dictionary.json")

# Play the anagram game
play_anagram_game(dictionary)
