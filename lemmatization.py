from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet
# nltk.download('omw-1.4')
# nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("walking"))
print(lemmatizer.lemmatize("walking", pos=wordnet.VERB))
print(lemmatizer.lemmatize("going"))
print(lemmatizer.lemmatize("going", pos=wordnet.VERB))
print(lemmatizer.lemmatize("ran", pos=wordnet.VERB))
print(lemmatizer.lemmatize("mice"))
