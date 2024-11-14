import ast
import re
import os
import gdown
from collections import defaultdict


with open('biword_counts.txt', 'r') as file:
    data = file.read()
    biword_counts = ast.literal_eval(data)

biword_counts = defaultdict(lambda: '1', biword_counts)

def remove_punctuation(text):
    # Remove punctuation marks and special characters
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

def remove_numbers(text):
    # Remove digits
    cleaned_text = re.sub(r'\d', '', text)
    return cleaned_text

def create_biwords(tokens):
    """
    Creates biwords from a list of tokens.
    Returns a list of biwords.
    """
    biwords = []
    for i in range(len(tokens) - 1):
        biword = tokens[i] + " " + tokens[i + 1]
        biwords.append(biword)
    return biwords

def consider_biwords(checking_sentences):
    if not os.path.exists("./biword_counts.txt"):
        url = 'https://drive.google.com/uc?id=1YUNtNSs-Rjq2MrSFXcmMQmA6_wSmIG24'
        output = 'biword_counts.txt'
        gdown.download(url, output, quiet=False)
    checked_sentences = []
    for sentence in checking_sentences:
        cleaned_sentence = remove_numbers(remove_punctuation(sentence[1]))
        tokens = cleaned_sentence.split()
        tokens.insert(0, '$')
        tokens.append('$')
        biwords = create_biwords(tokens)
        biword_value = 1
        for biword in biwords:
            biword_value *= int(biword_counts[biword])
        checked_sentences.append((biword_value * sentence[0],  sentence[1]))
    return list(sorted(checked_sentences, reverse=True))

#example
consider_biwords([(25, 'باید بدانیم'), (25, 'باید بدنیم')])
