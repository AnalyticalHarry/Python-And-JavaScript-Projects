from collections import Counter
import string

#function for word count
def word_count(filename, top_word_count=10):
    #opening the text file
    with open(filename, 'r') as file:
        #reading content into lower case
        content = file.read().lower()
        
        #removing punctuation and splitting the text into words
        words = content.translate(str.maketrans("", "", string.punctuation)).split()
        
        #counting the occurrences of each word
        words_count = Counter(words)
    
    #displaying the top N words and their frequencies
    for word, count in words_count.most_common(top_word_count):
        print(f"{word} : {count} times")
