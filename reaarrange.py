import random 

import sys
shuffle_words = []
def shuffle(words):
    
    for _ in range(len(words)):
        rando = words[random.randint(0,len(words)-1)]
        shuffle_words.append(rando)
        words.remove(rando)
    return shuffle_words

if __name__ == "__main__":
    word_list = sys.argv[1:]
    if len(word_list) == 1:
        word_list = list(word_list[0])
    random_words = shuffle(word_list)
    print(random_words) 
      



