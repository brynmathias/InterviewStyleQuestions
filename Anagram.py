#! /usr/bin/env python

def makeChrDict(word):
    if not isinstance(word,str): word = str(word)
    d = {}
    for l in word:
      if l == "\s": continue
      if l in d: d[l] +=1
      else: d[l] = 1
    return d


def isAnagram(word1, word2):
    d1 = makeChrDict(word1)
    d2 = makeChrDict(word2)
    for key in d2:
       if key in d1:
          if d2[key] > d1[key]:
	     return False
       else: return False
    return True

def anagram(word1 = str, word2 =str):
    chrArray1 = word1.split()
    for letter in word2:
        if letter is "\s": continue
	if letter not in chrArray1: return False
    return True
    #not yet complete as we don't check the number of each chr used.
listOfWords = [("mother in law","woman hitler"),("john mayer", "enjoy harm"),("president barack hussein obama a maniac presides", "the banks rob u"),("dog","cat"),(98574,75894)]


def main():
    for word1, word2 in listOfWords:
       if isAnagram(word1,word2): print word2, "is an anagram of ", word1
       else: print word2, "is not anagram of ", word1


if __name__ == "__main__":
   main()
