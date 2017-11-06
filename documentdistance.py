#!/usr/bin/python
#MEHMET TUGRUL SAVRAN
#2016 
import string
import sys
from math import *
from collections import defaultdict
    # math.acos(x) is the arccosine of x.
    # math.sqrt(x) is the square root of x.

# global variables needed for fast parsing
# translation table maps upper case to lower case and punctuation to spaces
translation_table = string.maketrans(string.punctuation+string.uppercase[0:26],
                                     " "*len(string.punctuation)+string.lowercase[0:26])

def read_file(filename):
    """ 
    Read the text file with the given filename;
    return a list of the lines of text in the file.
    """
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print "Error opening or reading input file: ",filename
        sys.exit()

def extract_words(filename):
    """
    Return a list of words from a file
    """
    lines = read_file(filename)
    lines = lines.translate(translation_table)
    return lines.split()

##############################################
## Count the frequency of each word ##
##############################################
def doc_dist(word_list1, word_list2):
    """
    Returns a float representing the document distance 
    in radians between two files when given the list of
    words from both files
    """
    

    dic1 = defaultdict(int)
    dic2 = defaultdict(int)

    for i in word_list1:
        dic1[i] += 1

    for i in word_list2:
        dic2[i] += 1

    #computing norm1
    norm1 = 0
    for i in dic1:
        norm1 += dic1[i]**2
    norm1 = sqrt(norm1)
    #computing norm2
    norm2 = 0 
    for i in dic2: 
        norm2 += dic2[i]**2
    norm2 = sqrt(norm2)

    #computing the dot product 
    dotproduct = 0 
    for i in dic1:
        if i in dic2:
            dotproduct += dic1[i]*dic2[i]

    denominator = float(norm1*norm2)

    ratio = (dotproduct/denominator)

    return float(acos(ratio))
    
##############################################
## Count the frequency of each pair ##
##############################################
def doc_dist_pairs(word_list1, word_list2):
    """
    Returns a float representing the document distance
    in radians between two files based on unique 
    consecutive pairs of words when given the list of
    words from both files
    """
    len1 = len(word_list1)
    pairlist1 = []
    for i in range(len1):
        if i+1 >= len1:
            break
        yip = " ".join(word_list1[i:i+2])
        pairlist1.append(yip)

    len2 = len(word_list2)
    pairlist2 = []
    for i in range(len2):
        if i+1 >= len2:
            break 
        yip2 = " ".join(word_list2[i:i+2])
        pairlist2.append(yip2)

    #initializing pair dictionaries 
    pairdic1 = defaultdict(int)
    pairdic2 = defaultdict(int)

    #counting frequencies for both frequency dictionaries
    for i in pairlist1:
        pairdic1[i] += 1 

    for i in pairlist2:
        pairdic2[i] += 1

    #computing norm1 and norm2
    norm1 = 0 
    for i in pairdic1: 
        norm1 += pairdic1[i]**2
    norm1 = sqrt(norm1)

    norm2 = 0
    for i in pairdic2: 
        norm2 += pairdic2[i]**2
    norm2 = sqrt(norm2)
    
    #computing the dot product 
    dotproduct = 0 
    for i in pairdic1:
        if i in pairdic2:
            dotproduct += pairdic1[i]*pairdic2[i]

    denominator = float(norm1*norm2)

    ratio = (dotproduct/denominator)

    return (acos(ratio))
    
    

#############################################################
## Count the frequency of the 50 most common words ##
#############################################################
def doc_dist_50(word_list1, word_list2):
    """
    Returns a float representing the document distance
    in radians between two files based on the 
    50 most common unique words when given the list of
    words from both files
    """
    #arbitrary top number 
    
    
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)

    for i in word_list1:
        dic1[i] += 1

    for i in word_list2:
        dic2[i] += 1

    sortlanmis1 = sorted(dic1.items(), key=lambda (k,v): k)
    sortlanmis2 = sorted(dic2.items(), key=lambda (k,v): k)

    sortlanmis1 = sorted(sortlanmis1, key=lambda (k,v): v, reverse = True)
    
    sortlanmis1 = sortlanmis1[:50]
    sortlanmis2 = sorted(sortlanmis2, key=lambda (k,v): v, reverse = True)
    
    sortlanmis2 = sortlanmis2[:50]

    #DID NOT CONFIGURE BREAKING THE TIES!!

    #--------#
    #computing norm1
    norm1 = 0
    for i in sortlanmis1:
        norm1 += i[1]**2
    norm1 = sqrt(norm1)

    #computing norm2
    norm2 = 0 
    for i in sortlanmis2:
        norm2 += i[1]**2
    norm2 = sqrt(norm2)

    dic1 = {}
    for i in sortlanmis1:
        dic1[i[0]] = i[1]

    dic2 = {}
    for i in sortlanmis2:
        dic2[i[0]] = i[1]

    #computing dot product

    dotproduct = 0

    for i in dic1:
        if i in dic2:
            dotproduct += dic1[i]*dic2[i]

    denominator = (norm1*norm2)

    ratio = (dotproduct/denominator)

    return (acos(ratio))

#Example Usage is shown below. Call extract_words with a txt file. It'll 
#output a list containing all the words inside the text (it is fast!) 
#Finally call doc_dist or doc_dist 50 or doc_dist_pairs with two 
#documents to be compared 

# tempest = extract_words("plays/tempest.txt")

# henry1 = extract_words("plays/henry_iv_1.txt")  

# henry2 = extract_words("plays/henry_iv_2.txt")   

# pirates = extract_words("plays/pirates_of_penzance.txt")


# henries = doc_dist(henry1,henry2)

# henriestop50 = doc_dist_50(henry1, henry2)

# henriespairs = doc_dist_pairs(henry1, henry2)

# print henries, henriestop50 , henriespairs


# henrytempest = doc_dist(henry1,tempest)

# henrytempesttop50 = doc_dist_50(henry1, tempest)

# henrytempestpairs = doc_dist_pairs(henry1, tempest)

# print henrytempest , henrytempesttop50 , henrytempestpairs 


# henrypirates = doc_dist(henry1,pirates)

# henrypiratestop50 = doc_dist_50(henry1, pirates)

# henrypiratespairs = doc_dist_pairs(henry1, pirates)

# print henrypirates, henrypiratestop50, henrypiratespairs






