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

def main(alphabet: list, discriminator: list, filepath: os.path):
    letter = random.choice(ALPHABET)
    number = str(random.randint(1000, 9999))
    disc = random.choice(discriminator)

    # Open the text file
    with open(FILE_PATH, "r") as f:
    # Set a random line (a random number from 0 to the count of lines)
        line_num = random.randint(0, sum(1 for _ in f)-1)
    
    word = linecache.getline(FILE_PATH, line_num)
    
    return letter+disc+number+disc+word.capitalize()

print(main(ALPHABET, DISCRIMINATOR, FILE_PATH))
