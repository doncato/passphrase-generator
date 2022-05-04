# Passphrase-Generator
A simple script to generate Passphrases that are Human readable while being moderately safe &amp; unique

This code has a function called `generate_passphrase` which returns a tuple of 3 strings
+ A random set of 5 chars where each one has 86 possibilities (e.g. `B>gh[`)
+ A number with 8 digits, or 2 blocks of 4 digits seperated by a '-' (each from 0-9) (e.g. `5260-7903`)
+ A random (newly) generated word from 3-14 characters that should be human-readable (more or less) (e.g. `Stuneiqui`)

## Installation & Execution
+ Download and install Python 3.5.x or higher on https://www.python.org/
+ Download the Script
+ Run the script using `python3 <path/to/script>` on UNIX Platforms or `py <path/to/script>`/`py3 <path/to/script>` on Windows

## Notes
+ You could theoratically use this as a library in other projects (`from passgen import generate_passphrase` and later use `generate_passphrase`)
