import json
import string
from hazm import Lemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import nltk
import os
import gdown

nltk.download('punkt')


def find_all_words_possible(word, first_letter_to_harf_mapping, letter_to_harf_mapping):
    converted_words = []
    j = 1
    if len(word) > 1 and word[0: 2] in first_letter_to_harf_mapping:
        j += 1
        for letters in first_letter_to_harf_mapping[word[0: 2]]:
            converted_words.append(letters)
    else:
        for letters in first_letter_to_harf_mapping[word[0]]:
            converted_words.append(letters)

    while j < len(word):
        if word[j] == word[j - 1]:
            j += 1
            continue
        new_converted_words = []
        if j + 1 < len(word) and word[j: j + 2] in letter_to_harf_mapping:
            for converted_word in converted_words:
                for letters in letter_to_harf_mapping[word[j: j+2]]:
                    new_converted_words.append(converted_word + letters)
            j += 1
        else:
            for converted_word in converted_words:
                for letters in letter_to_harf_mapping[word[j]]:
                    new_converted_words.append(converted_word + letters)
        converted_words = new_converted_words
        j += 1
    return converted_words


def sort_meaningful_words(words, words_tf):
    lemmatizer = Lemmatizer()
    new_words = []
    for word in words:
        lemmed_word = lemmatizer.lemmatize(word).split('#')[0]
        if lemmed_word in words_tf:
            new_words.append((words_tf[lemmed_word], word))
    new_words.sort(reverse=True)
    if len(new_words) == 0:
        return [(1, words[0])]
    return new_words


def load_dictionary(dict_path):
    words_tf = {}

    with open(dict_path, 'r', encoding='utf-8') as txt_file:
        for line in txt_file:
            parts = line.split('\t')
            words_tf[parts[0]] = int(parts[1])

    return words_tf


def translate_puncs(punc):
  if punc == ',':
      return '،'
  elif punc == ';':
      return '؛'
  elif punc == '?':
    return '؟'
  return punc


def find_all_sentences_sorted(words, first_letter_to_harf_mapping, letter_to_harf_mapping, words_tf):
    converted_sentences = [(1, '')]
    sentence_len = len(words)
    for word in  words:
        new_converted_sentences = []
        if word in string.punctuation:
            for converted_sentence in converted_sentences:
                converted_word = translate_puncs(word)
                new_converted_sentences.append((converted_sentence[0], converted_sentence[1].strip() + converted_word))
        else:
            converted_words = find_all_words_possible(word, first_letter_to_harf_mapping, letter_to_harf_mapping)
            converted_words = sort_meaningful_words(converted_words, words_tf)
            converted_words = converted_words[:3]
            for converted_sentence in converted_sentences:
                for converted_word in converted_words:
                    new_converted_sentences.append((converted_sentence[0] * (converted_word[0] ** (1/sentence_len)),
                                                converted_sentence[1].strip() + ' ' + converted_word[1]))
        converted_sentences = new_converted_sentences
    return list(sorted(converted_sentences, reverse=True))


def convert(text):
    if not os.path.exists("./biword_counts.txt"):
        url = 'https://drive.google.com/uc?id=1YUNtNSs-Rjq2MrSFXcmMQmA6_wSmIG24'
        output = 'biword_counts.txt'
        gdown.download(url, output, quiet=False)

    words_tf = load_dictionary('persian-wikipedia_lemmatized.txt')
    with open('letters_mapping.json', 'r', encoding='utf-8') as json_file:
        letter_to_harf_mapping = json.load(json_file)
    letter_to_harf_mapping = defaultdict(lambda: '.', letter_to_harf_mapping)

    with open('first_letters_mapping.json', 'r', encoding='utf-8') as json_file:
        first_letter_to_harf_mapping = json.load(json_file)

    words = word_tokenize(text)

    converted_sentences = find_all_sentences_sorted(words, first_letter_to_harf_mapping, letter_to_harf_mapping, words_tf)

    return converted_sentences

# usage example
s = convert('forsat ha, mesle aber 123.541 migozarand; bayad ghadreshan ra bedanim.')
print(s[0:10])
