"""Command-line utility to draw random words without repetition.

The script loads `words.txt` into memory and lets the user draw random
entries without repeats through a tiny command-line loop. Available
commands: `draw`, `restart`, and `exit`.
"""

import random

def pull_word(lst):
    """Print and remove one random word from the in-memory list.

    Args:
        lst (list[str]): Active pool of words.
    """
    rand_word = random_word(lst)
    print(rand_word)
    word_remove(lst,rand_word)

def word_remove(lst,w):
    """Remove a given word from the live pool.

    Args:
        lst (list[str]): Active pool of words.
        w (str): Word to remove.
    """
    lst.remove(w)

def random_word(lst):
    """Return a random word from the available list.

    Args:
        lst (list[str]): Active pool of words.

    Returns:
        str: Randomly selected word.
    """
    return(random.choice(lst))

def initialize_words():
    """Load the words from the local words.txt file.

    Returns:
        list[str]: Collection of candidate words.
    """
    try:
        with open('words.txt','r') as f:
            content = f.read()
            words = content.split(sep='\n')
        return words
    except:
        print("File words.txt missing")


def main():
    """Run the interactive loop until the user types exit."""
    words = initialize_words()

    # Keep asking for commands so the player can draw or restart.
    while True:
        key_word = input(
            'Select an option: '
        )

        #exit clause to leave tha game
        if key_word == 'exit':
            break

        #Restart words
        if key_word == 'restart':
            words = initialize_words()
            print('Words Generated!')

        if key_word == 'draw':
            if len(words)==0:
                print("Please initialize the list")
            else:
                pull_word(words)


if __name__ == '__main__':
    main()  
