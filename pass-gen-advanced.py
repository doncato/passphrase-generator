import os,random


def generate_word():
    # Variables
    # Maximum length of the generated word
    maximum_length = 14

    Consonants_combined = ['ch','st','sp','sch',]
    Consonants_single = ['b','c','d','f','g','h','j','k','l','m','n','p','qu','r','t','v','w','x','y','z']
    Consonants = Consonants_combined + Consonants_single
    Vowels = ['a','e','i','o','u','au','ei','ou','ui']
    all_letters = Consonants + Vowels

    word = []
    for i in range(maximum_length):
        if len(word) >= 1:
            if word[-1] in Consonants:
                letter = random.choice(Vowels)
            elif word[-1] in Vowels:
                letter = random.choice(Consonants)
        else:
            letter = random.choice(all_letters)
        word.append(letter)

    result = ''.join(word)
    word_length = random.randint(3,maximum_length)
    return result[:word_length].capitalize()

def generate_digits():
    Digits = ['0','1','2','3','4','5','6','7','8','9']
    number = []
    for i in range(8):
        number.append(random.choice(Digits))
    
    return f"{''.join(number[:4])}-{''.join(number[4:])}"

def generate_key():
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    characters_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','A','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    special_chars = ['+','-','_','*','#','$','%','&','<','>','(',')','[',']','=','?','!','^',',',';','.',':','/']
    chars = numbers + characters + characters_upper + special_chars

    result = []
    for i in range(5):
        result.append(random.choice(chars))

    return ''.join(result)

def generate_passphrase():
    return (generate_key(), generate_digits(), generate_word())

if __name__ == '__main__':
    print(' | '.join(generate_passphrase()))
