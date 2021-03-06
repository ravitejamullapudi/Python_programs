__author__ = 'Kalyan'

from placeholders import *
import string
notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names though :)
3. Try to use builtins and datastructures instead of writing your own.
4. If something about the function spec is not clear, use the corresponding test
   for clarification
'''
# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists, only use string functions
# assume words are separated by spaces.
def prune_either_or(sentence):
    if ('either' in sentence) and ('or' in sentence) :
        sentence = sentence.replace('either ','',1)
        sentence = sentence.split('or')
        sentence = string.lstrip(sentence[0])
        return sentence




# Create a palindrome of twice the length of the word passed in.
# e.g. app -> appppa, bat -> battab etc.
# hint: look up extended slice notation.
def create_palindrome(word):
    if word == None:
        return None
    if word == "":
        return ""
    else:
        return word+word[::-1]


# Sort the words that are passed in place by word length instead of word content.
# e.g ["apple", "dog", "elephant"] should return ["elephant", "apple", "dog"]
# no control flow statements.
def sort_by_length(words):
    if words == None:
        return None
    else:
        words.sort(key=len,reverse=True)
        return words




# return the top n most frequently occurring chars and their respective counts
# e.g aaaaaabbbbcccc, 2 should return [(a 5) (b 4)]
# in case of a tie, return char which comes earlier in alphabet ordering
# e.g. cdbba,2 -> [(b,2) (a,1)]
# use standard types and builtin functions 
def top_chars(word, n):
    from operator import itemgetter
    res = dict()
    for item in word:
        if res.has_key(item):
            res[item] +=1
        else:
            res[item] = 1
    res = tuple(res.items())
    res = sorted(res)
    res = sorted(res,key=itemgetter(1),reverse=True)
    res = res[:n]
    return res


# returns a dict which maps a -> 1, b -> 2 ... z->26 and A -> 1, B ->2 ... Z->26
# no control flow.
def get_encoding_dict():
    import string
    small = string.lowercase
    capital = string.uppercase
    res = dict(zip(list(small),list(range(1,27)))+zip(list(capital),list(range(1,27))))
    return res


def test_either_or_pruning():
    assert "We can go to a movie", prune_either_or("We can either go to a movie or a hotel")
    assert "We can go either way", prune_either_or("We can go either way")
    assert "" ==prune_either_or("either or")
    assert "either way is fine"   , prune_either_or("either way is fine")

def test_create_palindrome():
    assert "battab", create_palindrome("bat")
    assert "abba", create_palindrome("ab")
    assert ""==create_palindrome("")
    assert None == create_palindrome(None)

def test_sort_by_length():
    assert ["apple", "bear", "dog"] == sort_by_length(["dog", "apple", "bear"])
    assert ["apple", "bear", "dog"] == sort_by_length(["apple", "dog",  "bear"])
    assert ["apple", "dog", "cat"] == sort_by_length(["dog", "apple", "cat"])
    assert ["elephant", "apple"] == sort_by_length(["apple", "elephant"])
    assert ["three", "four", "one", "two"] == sort_by_length(["one", "two", "three", "four"])
    assert [] == sort_by_length([])
    assert None == sort_by_length(None)

def test_top_chars():
    assert [('p', 2)] == top_chars("app",1)
    assert [('p', 2), ('a',1)] == top_chars("app",2)
    assert [('p', 2), ('a',1)] == top_chars("app",3)

    assert [('a', 2)] == top_chars("aabc", 1)
    assert [('a', 2), ('b', 1)] == top_chars("aabc", 2)
    assert [('a', 2), ('b', 1), ('c', 1)] == top_chars("aabc", 3)

    assert [('e', 3)] == top_chars("irreversible", 1)
    assert [('e', 3), ('r', 3)] == top_chars("irreversible", 2)
    assert [('e', 3), ('r', 3), ('i',2), ('b', 1)] == top_chars("irreversible", 4)

def test_get_encoding_dict():
    d = get_encoding_dict()
    assert len(d) == 52
    for key in d:
        assert ord(key.lower()) - ord('a') + 1 == d[key]

three_things_i_learnt = """
- there are no cammas in the assertion statements
-
-
"""

time_taken_minutes = ___
