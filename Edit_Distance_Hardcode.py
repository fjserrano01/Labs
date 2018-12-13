#   Fernando Serrano, Instructor: Diego Aguirre, T.A.: Anindita Nath, 12/13/2018, CS 2302 DataStructures
#   This program is created to be able to determine the smallest amount of changes that need to be done
#   to two words in order to rewrite them to the same word. This is done with a matrix to store the value
#   of editing the letter and determines the value of the current change depending if the letters are similar;
#   storing the diagonal value in this location. The other change would be if the letters are different;
#   storing the min value of the locations preceding it and adding 1.
from Edit_Distance import edit_Distance


def main():
    word1 = "word"
    word2 = "fish"

    edit_Distance(word1, word2)

    word1 = "crab"
    word2 = "ran"
    edit_Distance(word1, word2)

    word1 = "fosh"
    word2 = "fish"
    edit_Distance(word1, word2)

    word1 = "canine"
    word2 = "arsanine"
    edit_Distance(word1, word2)


main()