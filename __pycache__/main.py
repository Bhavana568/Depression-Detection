##from nltk.stem import PorterStemmer 
##from nltk.tokenize import word_tokenize 
##   
##ps = PorterStemmer() 
##words = ["program", "programs", "programer", "programing", "programers"] 
##  
##for w in words: 
##    print(w, " : ", ps.stem(w)) 
##------------------------------------------------------------------------------------------------------------------------------------------------
##from nltk.corpus import stopwords 
##from nltk.tokenize import word_tokenize 
##
##example_sent = "Dave watched as the forest burned up on the hill, only a few miles from her house. The car had been hastily packed and Marta was inside trying to round up the last of the pets. Dave went through his mental list of the most important papers and documents that they couldn't leave behind. He scolded himself for not having prepared these better in advance and hoped that he had remembered everything that was needed. He continued to wait for Marta to appear with the pets, but she still was nowhere to be seen."
##  
##stop_words = set(stopwords.words('english')) 
##
##word_tokens = word_tokenize(example_sent) 
##
##filtered_sentence = [w for w in word_tokens if not w in stop_words] 
##
##for w in word_tokens: 
##	if w not in stop_words: 
##		filtered_sentence.append(w) 
##
##print(word_tokens) 
##print(filtered_sentence) 
##------------------------------------------------------------------------------------------------------------------------------------------------
##import nltk
##from nltk.corpus import stopwords
##print(stopwords.words('english'))

##------------------------------------------------------------------------------------------------------------------------------------------------

## from textblob lib. import TextBlob method 
##from textblob import TextBlob 
##
##text = "Dave watched as the forest burned up on the hill, only a few miles from her house. The car had been hastily packed and Marta was inside trying to round up the last of the pets. Dave went through his mental list of the most important papers and documents that they couldn't leave behind. He scolded himself for not having prepared these better in advance and hoped that he had remembered everything that was needed. He continued to wait for Marta to appear with the pets, but she still was nowhere to be seen."
##  
## create a TextBlob object 
##object = TextBlob(text) 
##
## into words. 
##print(" Word Tokenize :\n", object.words) 
##
## into sentences. 
##print("\n Sentence Tokenize :\n", object.sentences)

##------------------------------------------------------------------------------------------------------------------------------------------------

##from nltk.tokenize import sent_tokenize, word_tokenize 
##  
##text = "Dave watched as the forest burned up on the hill, only a few miles from her house. The car had been hastily packed and Marta was inside trying to round up the last of the pets. Dave went through his mental list of the most important papers and documents that they couldn't leave behind. He scolded himself for not having prepared these better in advance and hoped that he had remembered everything that was needed. He continued to wait for Marta to appear with the pets, but she still was nowhere to be seen."
##  
##print(sent_tokenize(text)) #seperates at puncuation
##print(word_tokenize(text)) #seperates at space

##------------------------------------------------------------------------------------------------------------------------------------------------

##from nltk.tokenize import SpaceTokenizer  
##a = SpaceTokenizer() 
##s = "Good morning Dishitaa here!"
##ans = a.tokenize(s) 
##     
##print(ans)

##------------------------------------------------------------------------------------------------------------------------------------------------

##from nltk.stem import WordNetLemmatizer 
##  
##lemmatizer = WordNetLemmatizer() 
##  
##print("chocolates :", lemmatizer.lemmatize("chocolates")) 
##print("better :", lemmatizer.lemmatize("better", pos ="a"))

##------------------------------------------------------------------------------------------------------------------------------------------------
# TabTokenizer works on \t and tokenizes at \t
# tokenize works on space and tokenizes at a space

##from nltk.tokenize import TabTokenizer
##x=TabTokenizer()
##text2="hi\tdee\t,,,,......\tkihsenkw0"
##print(x.tokenize(text2))

##------------------------------------------------------------------------------------------------------------------------------------------------
from nltk.tokenize import word_tokenize
text = "Her mom had warned her."
print(word_tokenize(text))
##------------------------------------------------------------------------------------------------------------------------------------------------
