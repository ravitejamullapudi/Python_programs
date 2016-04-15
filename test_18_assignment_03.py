__author__ = 'Kalyan'

# http://en.wikipedia.org/wiki/Scrabble_letter_distributions

from placeholders import *

scrabble_scores = [ (1, "EAOINRTLSU"), (2, "DG"), (3, "BCMP"),
                    (4, "FHVWY"), (5, "K"), (8, "JX"), (10, "QZ")]

#return a dict which contains a letter to score mapping.
#use dict comprehensions
def get_scrabble_scorer():
    return { z: x for x,y in scrabble_scores for z in y}


def test_scrabble_scorer():
    score_dict = get_scrabble_scorer()
    for score,letters in scrabble_scores:
        for letter in letters:
            assert score == score_dict.get(letter)

# instead of returning a list of tuples like zip, generate it incrementally
# a tuple at a time. Use exception control flow to write elegant code.
def generator_zip(seq1, seq2, *more_seqs):
    pass


def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    for x in range(3):
        assert (x,x,x,x) == next(gen)

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___