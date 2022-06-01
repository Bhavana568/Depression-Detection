### import these modules 
##from nltk.stem import WordNetLemmatizer 
##
##lemmatizer = WordNetLemmatizer() 
##
##print("rocks :", lemmatizer.lemmatize("rocks")) 
##print("corpora :", lemmatizer.lemmatize("corpora")) 
##
### a denotes adjective in "pos" 
##print("better :", lemmatizer.lemmatize("better", pos ="a"))

#-------------------------------------------------------------------------------------------------------------------------------------------------

import nltk
nltk.download('wordnet') 
from nltk.stem import WordNetLemmatizer 

# Create WordNetLemmatizer object 
wnl = WordNetLemmatizer() 

# single word lemmatization examples 
list1 = ['kites', 'babies', 'dogs', 'flying', 'smiling', 
		'driving', 'died', 'tried', 'feet'] 
for words in list1: 
	print(words + " ---> " + wnl.lemmatize(words)) 
	
#> kites ---> kite 
#> babies ---> baby 
#> dogs ---> dog 
#> flying ---> flying 
#> smiling ---> smiling 
#> driving ---> driving 
#> died ---> died 
#> tried ---> tried 
#> feet ---> foot

# sentence lemmatization examples 
string = 'the cat is sitting with the bats on the striped mat under many flying geese'

# Converting String into tokens 
list2 = nltk.word_tokenize(string) 
print(list2) 
#> ['the', 'cat', 'is', 'sitting', 'with', 'the', 'bats', 'on', 
# 'the', 'striped', 'mat', 'under', 'many', 'flying', 'geese'] 

lemmatized_string = ' '.join([wnl.lemmatize(words) for words in list2]) 

print(lemmatized_string) 
#> the cat is sitting with the bat on the striped mat under many flying goose


#-------------------------------------------------------------------------------------------------------------------------------------------------

# WORDNET LEMMATIZER (with appropriate pos tags) 

##import nltk 
##from nltk.stem import WordNetLemmatizer 
##nltk.download('averaged_perceptron_tagger') 
##from nltk.corpus import wordnet 
##
##lemmatizer = WordNetLemmatizer() 
##
### Define function to lemmatize each word with its POS tag 
##
### POS_TAGGER_FUNCTION : TYPE 1 
##def pos_tagger(nltk_tag): 
##	if nltk_tag.startswith('J'): 
##		return wordnet.ADJ 
##	elif nltk_tag.startswith('V'): 
##		return wordnet.VERB 
##	elif nltk_tag.startswith('N'): 
##		return wordnet.NOUN 
##	elif nltk_tag.startswith('R'): 
##		return wordnet.ADV 
##	else:		 
##		return None
##
##sentence = 'the cat is sitting with the bats on the striped mat under many badly flying geese'
##
### tokenize the sentence and find the POS tag for each token 
##pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence)) 
##
##print(pos_tagged) 
###>[('the', 'DT'), ('cat', 'NN'), ('is', 'VBZ'), ('sitting', 'VBG'), ('with', 'IN'), 
### ('the', 'DT'), ('bats', 'NNS'), ('on', 'IN'), ('the', 'DT'), ('striped', 'JJ'), 
### ('mat', 'NN'), ('under', 'IN'), ('many', 'JJ'), ('flying', 'VBG'), ('geese', 'JJ')] 
##
### As you may have noticed, the above pos tags are a little confusing. 
##
### we use our own pos_tagger function to make things simpler to understand. 
##wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged)) 
##print(wordnet_tagged) 
###>[('the', None), ('cat', 'n'), ('is', 'v'), ('sitting', 'v'), ('with', None), 
### ('the', None), ('bats', 'n'), ('on', None), ('the', None), ('striped', 'a'), 
### ('mat', 'n'), ('under', None), ('many', 'a'), ('flying', 'v'), ('geese', 'a')] 
##
##lemmatized_sentence = [] 
##for word, tag in wordnet_tagged: 
##	if tag is None: 
##		# if there is no available tag, append the token as is 
##		lemmatized_sentence.append(word) 
##	else:		 
##		# else use the tag to lemmatize the token 
##		lemmatized_sentence.append(lemmatizer.lemmatize(word, tag)) 
##lemmatized_sentence = " ".join(lemmatized_sentence) 
##
##print(lemmatized_sentence) 
###> the cat can be sit with the bat on the striped mat under many fly geese
##

#-------------------------------------------------------------------------------------------------------------------------------------------------

##from textblob import TextBlob, Word 
##
##my_word = 'cats'
##
### create a Word object 
##w = Word(my_word) 
##
##print(w.lemmatize()) 
###> cat 
##
##sentence = 'the bats saw the cats with stripes hanging upside down by their feet.'
##
##s = TextBlob(sentence) 
##lemmatized_sentence = " ".join([w.lemmatize() for w in s.words]) 
##
##print(lemmatized_sentence) 
###> the bat saw the cat with stripe hanging upside down by their foot

#-------------------------------------------------------------------------------------------------------------------------------------------------

##from textblob import TextBlob 
##
### Define function to lemmatize each word with its POS tag 
##
### POS_TAGGER_FUNCTION : TYPE 2 
##def pos_tagger(sentence): 
##	sent = TextBlob(sentence) 
##	tag_dict = {"J": 'a', "N": 'n', "V": 'v', "R": 'r'} 
##	words_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]	 
##	lemma_list = [wd.lemmatize(tag) for wd, tag in words_tags] 
##	return lemma_list 
##
### Lemmatize 
##sentence = "the bats saw the cats with stripes hanging upside down by their feet"
##lemma_list = pos_tagger(sentence) 
##lemmatized_sentence = " ".join(lemma_list) 
##print(lemmatized_sentence) 
###> the bat saw the cat with stripe hang upside down by their foot 
##
##lemmatized_sentence = " ".join([w.lemmatize() for w in t_blob.words]) 
##print(lemmatized_sentence) 
###> the bat saw the cat with stripe hanging upside down by their foot

#-------------------------------------------------------------------------------------------------------------------------------------------------

