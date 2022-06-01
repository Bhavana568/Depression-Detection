#TOKENIZATION CODE
#tokenizing - word and sentence
#lexicon - dictionary(word and meanings)
#corpora - body of text

#------------------------------------------------------------------------------------------------------------------------------------------------------

##from nltk.tokenize import sent_tokenize, word_tokenize
##example_text = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
##print(sent_tokenize(example_text))
##print(word_tokenize(example_text))
##for i in word_tokenize(example_text):
##    print (i)

#------------------------------------------------------------------------------------------------------------------------------------------------------

### import SyllableTokenizer() method from nltk 
##from nltk import word_tokenize 
##     
### Create a reference variable for Class word_tokenize 
##tk = SyllableTokenizer() 
##     
### Create a string input 
##pqr = "Antidisestablishmentarianism"
##     
### Use tokenize method 
##abc = tk.tokenize(pqr) 
##     
##print(abc)

#------------------------------------------------------------------------------------------------------------------------------------------------------

##from nltk.tokenize import RegexpTokenizer 
##    
### Create a reference variable for Class RegexpTokenizer 
##tk = RegexpTokenizer('\s+', gaps = True) 
##    
### Create a string input 
##gfg = "I love Python"
##    
### Use tokenize method 
##geek = tk.tokenize(gfg) 
##    
##print(geek)

#------------------------------------------------------------------------------------------------------------------------------------------------------

### import TabTokenizer() method from nltk 
##from nltk.tokenize import TabTokenizer 
##     
### Create a reference variable for Class TabTokenizer 
##tk = TabTokenizer() 
##     
### Create a string input 
##gfg = "Geeksfor\tGeeks..\t.$$&* \nis\t for geeks"
##     
### Use tokenize method 
##geek = tk.tokenize(gfg) 
##     
##print(geek)

#------------------------------------------------------------------------------------------------------------------------------------------------------

# import TweetTokenizer() method from nltk 
from nltk.tokenize import TweetTokenizer 
  
# Create a reference variable for Class TweetTokenizer 
tk = TweetTokenizer() 
  
# Create a string input 
gfg = "Geeks for Geeks"
  
# Use tokenize method 
geek = tk.tokenize(gfg) 
  
print(geek)
