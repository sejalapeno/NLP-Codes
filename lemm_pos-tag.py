
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet

from lemmatization import lemmatizer

nltk.download('omw-1.4')
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger')

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


sentence = "Donald Trump has a devoted following".split()

words_and_tags = nltk.pos_tag(sentence)
print(words_and_tags)

for word,tag in words_and_tags:
    lemma=lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag))
    print(lemma,end=" ")