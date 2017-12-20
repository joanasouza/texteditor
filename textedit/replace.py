def replace_words(words):
    with open(words, 'r') as input:
        with open('new_alice.txt', 'w') as output:
            for line in input:
                line = line.rstrip()
                newline = line.replace("Alice", "Dora the Explorer")
                print(newline)
                output.write(newline)


if __name__ == '__main__':
    replace_words('alice.txt')
            
