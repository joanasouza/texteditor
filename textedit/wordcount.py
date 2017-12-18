'''
Takes a file as sys.arg[1] as input and returns a wordcount,
character count, and sentence count.
'''
import re
import sys
import os

class WC:

    '''Conducts character, word, and letter count of object'''

    def __init__(self, filename):
        self.filename = filename


    def open_file(self, filename):
        '''
        Opens a file object, reads and returns your content
        '''
        with open(filename, 'r') as file:
            file_contents = file.read()
            return file_contents


    def word_count(self):
        '''
        Returns a file's word count
        '''
        wc_file = self.open_file(self.filename)
        self = len(wc_file.split())
        return ('Total words: ',len(wc_file.split()))


    def sentence_count(self):
        '''
        Returns a file's sentence count
        '''
        sc_file = self.open_file(self.filename)
        return ('Total sentences:' , sc_file.count('.')+ sc_file.count('?') + sc_file.count('!'))

    
    def  letter_count(self):
        '''
        Returns a file's character count, excluding punctuation
        '''
        letter_counter = 0
        pattern = r'[\W]' # excludes all punctuation
        cc_file = self.open_file(self.filename)
        total_words = cc_file.split()

        for word in total_words:
            for letter in word:
                if not re.search(pattern, letter):
                    letter_counter += 1

        return ("Letters:", letter_counter)


    def counts(self):
        print(self.word_count(), '\n', self.sentence_count(), '\n', self.letter_count())


if __name__ == '__main__':
    alice = WC(sys.argv[1])
    WC.counts(alice)
