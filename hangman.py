# Problem Set 2, hangman.py
# Name: Shapovalov Gleb
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    secret_word = secret_word
    letters_guessed = letters_guessed
    secret_word = set(secret_word)
    letters_guessed = set(letters_guessed)
    return secret_word <= letters_guessed


def get_guessed_word(secret_word, letters_guessed):
    if set(secret_word) <= set(letters_guessed):
        secret_word = ' '.join(list(secret_word))
    else:
        for a in secret_word:
            if a not in letters_guessed:
                secret_word = secret_word.replace(a, '_')
        secret_word = ' '.join(list(secret_word))
    print('Вгадані букви:', secret_word)
    return secret_word


def get_guessed_word_2(secret_word, letters_guessed):
    if set(secret_word) <= set(letters_guessed):
        secret_word = ' '.join(list(secret_word))
    else:
        for a in secret_word:
            if a not in letters_guessed:
                secret_word = secret_word.replace(a, '_')
        secret_word = ' '.join(list(secret_word))
    return secret_word


def get_available_letters(letters_guessed):
    import string
    a = letters_guessed
    string = string.ascii_lowercase
    for i in a:
        if i in string:
            string = string.replace(i, '')
    print('Букви, які ти ще не провіряв(-ла):', string)


def guesses_remaining(letter, guesses_remaining):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        guesses_remaining = (guesses_remaining - 2)
    else:
        guesses_remaining = (guesses_remaining - 1)
    print(guesses_remaining)
    return guesses_remaining


def input_letters(letters_guessed, remaining):
    global warns
    letter = input('Введи своє припущення: ')
    letter = str.lower(letter)
    if len(letter) != 1:
        print('Ти ввiв(-ела) більше одного символe або добавив пробіл!')
        warn(remaining, 0)
        return input_letters(letters_guessed, remaining)
    elif len(letter) == 1:
        if ord(letter) not in range(97, 123):
            print('Вводити треба тільки літери латинського алфавіту')
            warn(remaining, 0)
            return input_letters(letters_guessed, remaining)

    return letter


warns = 3


def warn(remaining, warns_type):
    global warns
    warns = warns - 1
    if warns_type == 0:
        print('Мінус одне попередження, друже!')
    if warns_type == 1:
        print('Ти вже перевіряв цю букву!')
    if warns == 0:
        print('Опа! В тебе не залишилось попереджень! Мінус одна спроба!')
        remaining = remaining - 1
    if warns == -1:
        warns = 0
    return warns


print('Привіт, людино! Зіграємо в гру? Я загадав слово, а ти попробуй його вгадати.')


def hangman(secret_word):
    letters_guessed = []
    remaining = 6
    print('Довжина мого слова: ', len(secret_word))
    while remaining > 0:
        print('В тебе є', remaining, 'спроб(-и) та', warns, 'попередження(-ень)')
        get_available_letters(letters_guessed)
        letter = input_letters(letters_guessed, remaining)
        if letter in list(secret_word):
            if letter in letters_guessed:
                print('Ти вже вгадав цю букву!\n------------------------------------')
                continue
            print('Ого, повезло! Ти вгадав(-ла) букву!')
        else:
            print('Ха-ха! Не влучив(-ла)! Нема такої букви в моєму слові')
            if letter in letters_guessed:
                warn(remaining, 1)

            if letter not in list(secret_word):
                if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                    remaining = remaining - 2


                else:
                    remaining = remaining - 1

        letters_guessed.append(letter)
        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Добре-добре, ти вгадав слово... Молодець!')
            print('Слово, яке я загадав: ', secret_word)
            print('Твій рахунок:', len(set(secret_word)) * remaining)
            break
        get_guessed_word(secret_word, letters_guessed)
        print('\n', '------------' * 3, '\n')
    return remaining


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    s = my_word.split()
    s_1 = my_word.replace('_', '').split()
    l = other_word.replace('', ' ').split()
    lst = []
    if len(s) == len(l):
        for i in range(len(s)):
            if s[i] == '_':
                continue
            if s[i] == l[i]:
                lst.append(l[i])
        if lst == s_1:
            return True
        elif lst != s_1:
            return False
    else:
        return False


def show_possible_matches(my_word):
    lst = []

    for i in wordlist:
        c = match_with_gaps(my_word, i)
        if c == True:
            lst.append(i)
            string = ' '.join(lst)
    print('------------------------------------\nМожливі слова: ', string, '\n')


def input_letters_hints(letters_guessed, remaining):
    global warns
    letter = input('Введи своє припущення: ')
    letter = str.lower(letter)
    if len(letter) != 1:
        print('Ти ввiв(-ела) більше одного символe або добавив пробіл! Або зовсім нічого не ввів')
        warn(remaining, 0)
        return input_letters(letters_guessed, remaining)
    elif len(letter) == 1:
        if ord(letter) not in range(97, 123) and letter != '*':
            print('Вводити треба тільки літери латинського алфавіту та символ "*" для виклику підсказок!')
            warn(remaining, 0)
            return input_letters(letters_guessed, remaining)
    return letter


def hangman_with_hints(secret_word):
    letters_guessed = []
    remaining = 6
    print('Довжина мого слова: ', len(secret_word))
    while remaining > 0:
        my_word = get_guessed_word_2(secret_word, letters_guessed)
        print('В тебе є', remaining, 'спроб(-и) та', warns, 'попередження(-ень)')
        get_available_letters(letters_guessed)
        letter = input_letters_hints(letters_guessed, remaining)
        if letter in list(secret_word):
            if letter in letters_guessed:
                print('Ти вже вгадав цю букву!\n------------------------------------')
                warn(remaining, 1)
            else:
                print('Ого, повезло! Ти вгадав(-ла) букву!')
            if letter == '*':
                show_possible_matches(my_word)

        else:
            if letter == '*':
                show_possible_matches(my_word)
            elif letter != '*':
                if letter in letters_guessed and letter != '*':
                    warn(remaining, 1)
                else:
                    print('Ха-ха! Не влучив(-ла)! Нема такої букви в моєму слові')
                if letter not in list(secret_word):
                    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                        print('Введена неправильна голосна буква. Мінус дві спроби!')
                        remaining = remaining - 2
                    else:
                        print('Введена неправильна приголосна буква. Мінус спроба!')
                        remaining = remaining - 1
        if letter != '*':
            letters_guessed.append(letter)
        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Добре-добре, ти вгадав слово... Молодець!')
            print('Слово, яке я загадав: ', secret_word)
            print('Твій рахунок:', len(set(secret_word)) * remaining)
            break
        get_guessed_word(secret_word, letters_guessed)
        print('\n', '------------' * 3, '\n')
    return remaining


def game(secret_word):
    c = hangman_with_hints(secret_word)
    if c <= 0:
        print('Ти програв(-ла)! Не вгадав слово. Ще раз? ')
        print('Моїм словом було:', secret_word)
        qstn = input('Продовжити?(Y - так, будь-який інший символ - ні) ')
        if qstn == 'Y' or qstn == 'y':
            return game(secret_word)
        else:
            print('Допобачення!')
    else:
        qstn = input('Продовжити гру?(Y - так, будь-який інший символ - ні) ')
        if qstn == 'Y' or qstn == 'y':
            return game(secret_word)
        else:
            print('Допобачення!')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    game(secret_word)
