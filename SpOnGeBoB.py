"""sPoNgEcAsE program. Speak like the mocking spongebob meme with ease using this program.

Simply type normal text and the program will spit out the mocking variation for you :) 
Tags: tiny, beginner, project, starter, python"""

import random

try:
    import pyperclip #pyperclip copies text top the clipboard
except ImportError:
    pass # If pyperclip is not installed, do nothing. It's no big deal

def main():
    """Run the spongetext program"""
    print('''sPoNgEcAsE, bY mOnEtiZaTiOn AnDy AnDy@MoNeTiZAtIoNmAcHiNe.CoM
eNtEr YoUr MesSAgE''')

    spongetext = english_to_spongecase(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass # Do nothing if pyperclip wasn't installed

def english_to_spongecase(message):
    """Return the spongetext form of the given string."""
    spongetext = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongetext += character
            continue

        if useUpper:
            spongetext += character.upper()
        else:
            spongetext += character.lower()

        # Flip the case, 90% of the time for apparent randomness
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper # Flips the case
    return spongetext

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()