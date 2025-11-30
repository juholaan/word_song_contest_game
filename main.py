import random

def pull_word(lst):
    rand_word = random_word(lst)
    print(rand_word)
    word_remove(lst,rand_word)

def word_remove(lst,w):
    lst.remove(w)

def random_word(lst):
    return(random.choice(lst))

def initialize_words():
    with open('words.txt','r') as f:
        content = f.read()
        words = content.split(sep='\n')
    return words

def main():
    words = initialize_words()

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
                "Please initialize the list"
            else:
                pull_word(words)


if __name__ == '__main__':
    main()  