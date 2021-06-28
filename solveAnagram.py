from typing import Dict
import nltk
from nltk.corpus import words as dict

def solveAnagram(letters):
    results = []
    for word in dict.words():
        if len(word) <= len(letters) and len(word) >= 3:
            chars = list(word.lower())
            temp = list(letters)
            invalid = False
            for char in chars:
                if char in temp:
                    idx = temp.index(char)
                    temp.pop(idx)
                else:
                    invalid = True
                    break
            if not invalid:
                results.append(word)
    return results

def sortAnagramList(anagrams):
    anagramLower = map(str.lower, anagrams)
    return sorted(list(Dict.fromkeys(anagramLower)), key=len)

def main():
    nltk.download('words', quiet=True)
    
    while True:
        letters = input('Enter letters (press enter only to quit): ')
        if len(letters) == 0:
            return
        
        a = solveAnagram(letters)
        b = sortAnagramList(a)
        print(b)

if __name__ == "__main__":
    main()