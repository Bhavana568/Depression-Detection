### import these modules 
##from nltk.stem import PorterStemmer 
##from nltk.tokenize import word_tokenize 
##
##ps = PorterStemmer() 
##
### choose some words to be stemmed 
##words = ["program", "programs", "programer", "programing", "programers"] 
##
##for w in words: 
##	print(w, " : ", ps.stem(w)) 

##-------------------------------------------------------------------------------------------------------------------------------------

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
##example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
##for w in example_words:
##    print(ps.stem(w))
new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)

