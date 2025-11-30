def get_words():
    with open('words.txt','r') as f:
        content = f.read()
        words = content.split(sep='\n')
    return words

def main():
    get_words()

if __name__ == '__main__':
    main()