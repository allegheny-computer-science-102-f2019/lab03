#!/usr/bin/env python3

# Date = 19 Sept 2019
# Version = i
# OriginalAuthor =

# Description: A program to model two speakers who exchange a "meaningful" conversation between each other.

stopWords_list =["I", "have","know", "like", "love", " to ", " a "]
# we remove stop words as they do not add specificity to the strings

aliceVocab_list = ["I gave carrots to horses","I like cats"] # add more calls here
bobVocab_list = [] # add responses here

def removeStopWords(in_str):
    """ used to remove the words which do not add to the meaning of the calls and responses"""
    for s in stopWords_list:
        in_str = in_str.replace(s,"")
   # print("removeStopWords(), return statement: ",in_str,type(in_str) )
    return in_str.strip() # return the line without the stop words to the caller
#end of removeStopWords()

def main():
    speakerAlice()
    speakerBob()
#TODO

#end of main()


def speakerAlice(): #you will need input parameters here
    print(" This is Alice!")
    aliceSays_str = random.choice(aliceVocab_list)# choose some random element from the list
    print("  This is Alice. I say to Bob :", aliceSays_str)

#TODO
#end of speakerA()

def speakerBob(): #you will need input parameters here
    print(" This is Bob!")
#TODO
#end of speakerA()

import random
main() # runs the program
