import random
from typing import List
from typing import Set

answers = List[str] #each word diffrent letters
answers_now : answers = ['agnes', 'alpha', 'omega', 'chest', 'quest', 'magic', 'actor' , 'kites' , 'admit', 'adore', 'marie', 'chaos', 'china', 'disco', 'faint', 'paint', 'march', 'flowy', 'manic', 'petal', 'zebra', 'royal', 'shake', 'young', 'youth']


def choose_word(l : answers)->str:
    """ """
    n : int = int((len(l))*random.random())
    word : str = l[n]
    return  word

def word_into_list(w : str)->List[str]:
    """ """
    return [c for c in w]

assert word_into_list('agnes') == ['a','g','n','e','s']
assert word_into_list('green') == ['g','r','e','e','n']

def list_into_word(l : List[str])->str:
    """ """
    s : str = ''
    e : str
    for e in l:
        s = s + e
    return s

assert list_into_word(['a','g','n','e','s']) == 'agnes'
assert list_into_word(['g','r','e','e','n']) == 'green'

def two_letters(w : str)->bool:
    """ if there are two the same letters in a word, return true """
    seen : Set[str] = set()
    c : str
    for c in w:
        if c in seen:
            return True
        else:
            seen.add(c)
    return False

def check_and_feedback(user_word: str, chosen_word : str)->List[str]:
    """checks if every letters if right and returns for ex [n, False, wrong-place]"""

    if two_letters(user_word):
        return ['There cannot be two the same letters in a word']
    
    chosen_set : Set[str] = {c for c in chosen_word}
    res : List[str] = []
    i : int
    for i in range(len(user_word)):
        
        if user_word[i]==chosen_word[i]:
            res.append(user_word[i])
            
        elif user_word[i]!=chosen_word[i]:
            if user_word[i] in chosen_set:
                res.append('wrong place')
            else:
                res.append('false')
    return res

assert check_and_feedback('agees','agnes') == ['There cannot be two the same letters in a word']
assert check_and_feedback('agnes','agnes') == ['a','g','n','e','s']
assert check_and_feedback('natle','agnes') == ['wrong place', 'wrong place', 'false', 'false', 'wrong place']

def guessed(u : str, w : str)->bool:
    """ if word is guessed return true"""
    return u == w

def wordle(l : answers):
    """ """
    print("\nYou have to guess the word within 6 rounds. A word contains 5 letters. There cannot be two of the same letters in a word\n")
    print("Good luck!")
    secret_word : str = choose_word(l)
    i : int
    for i in range(6):
        user : str = input()
        if user == secret_word:
            return print(secret_word, "is the right answer! Good job<3")
        else: 
            print(check_and_feedback(user, secret_word))
    
    return print(secret_word, "was the answer! Better luck next time <3")

def play_wordle():
    wordle(answers_now)

