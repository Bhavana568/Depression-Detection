##import re
##text = "This &is [an] example? {of} 'string'. with.? Punctuation!!!!"
##print(re.sub('[^A-Za-z0-9]+', ' ', text))


import re
text = "This &is [an] example? {of} 'string'. with.? Punctuation!!!!"
print(re.sub('[^A-Za-z0-9]+', ' ', text))
