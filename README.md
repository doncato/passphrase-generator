# Passphrase-Generator
A simple script to generate Passphrases that are Human readable while being moderately safe &amp; unique

## Safety
The possibilities of combinations can be calculated by multiplying the possibilities of each 'field'
Meaning There are as much possible phrases as:<br>
__[Count of Descriminators] * [Length of the Alphabet] * [Length of possible Numbers] * [Count of possible words]__

With the default, provided values this leaves
~1.4*10^12 possibilities
**Please note that I am not a security expert**

## Installation & Execution
+ Download and install Python 3.5.x or higher on https://www.python.org/
+ Download the Script and the words.txt
+ Run the script using `python3 <path/to/script>` on UNIX Platforms or `py <path/to/script>`/`py3 <path/to/script>` on Windows

## Notes
+ You can change the Constants at the top in the main.py file as you wish
+ The provided words.txt could be provided thanks to https://github.com/dwyl/english-words/
