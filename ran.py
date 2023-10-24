import nltk
import random

# Download the WordNet data if you haven't already
nltk.download('wordnet')

# Import WordNet
from nltk.corpus import wordnet

def generate_random_verb():
    # Get all verb synsets from WordNet
    verb_synsets = list(wordnet.all_synsets(pos=wordnet.VERB))
    
    # Extract verbs from the synsets
    verbs = [lemma.name() for synset in verb_synsets for lemma in synset.lemmas()]
    
    # Filter out duplicate verbs
    unique_verbs = list(set(verbs))
    
    # Select a random verb
    random_verb = random.choice(unique_verbs)
    
    return random_verb

# Usage example: generate a random verb
random_verb = generate_random_verb()
