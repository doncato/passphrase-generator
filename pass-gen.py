import os,random,linecache

###############################################################
# Settings / Constants
# Feel free to change these

# The discriminators used to combine all 'fields'
DISCRIMINATOR = ['-&-', '-', '/', '+', '&']
# The Greek Alphabet
ALPHABET = ['Alpha','Beta','Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega']
# The file path to the text encoded file containing words
FILE_PATH = os.path.join(os.path.dirname(__file__),"words.txt")

###############################################################

def generate(alphabet: list, discriminator: list, filepath: os.path):
    """
    Generate a random passphrase

    generate(list, list, os.path) -> str
    # Arguments:
    alphabet: a list containing string elements that can be used as the first part
    discriminator: a list containing string elements one of which will be randomly choosed to combine all parts with each other
    filepath: an os.path to a text file containing a newline seperated list of possible words

    # Returns:
    A random string consisting of <a Random Element of 'alphabet'><a Random 'discriminator'><4 random digits><the same 'discriminator'><a Random line from the text file>

    # Notes:
    The case of the words is differently set, there are 3 possibilities: Foo, FOO, foo
    """

    letter = random.choice(ALPHABET)
    number = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
    disc = random.choice(discriminator)

    case = random.randint(0, 2)
    # Open the text file
    with open(FILE_PATH, "r") as f:
    # Set a random line (a random number from 0 to the count of lines)
        line_num = random.randint(0, sum(1 for _ in f)-1)
    
    word = linecache.getline(FILE_PATH, line_num)
    
    if case == 0:
        letter = letter.upper()
        word = word.upper()
    elif case == 1:
        letter = letter.lower()
        word = word.lower()
    elif case == 2:
        letter = letter.capitalize()
        word = word.capitalize()

    return letter+disc+number+disc+word

if __name__ == "__main__":
    print(generate(ALPHABET, DISCRIMINATOR, FILE_PATH))