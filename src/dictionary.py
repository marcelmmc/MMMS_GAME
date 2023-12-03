from typing import List
import json
import os
import random
import pickle
import re
import random
import pickle
import numpy as np

class DictionaryError(Exception):
    def __init__(self, message: str):
        super(message)

dictionaries_cache = {}
repo = os.path.dirname(os.path.dirname(__file__))
class Dictionary:
    """A class representing a dictionary"""
    dictionaries_path = os.path.join(
        repo,
        "dictionaries"
    )

    def __init__(self, path: str, name: str, words: List[str], percentage_missing_words=0):
        self.path = path
        self.name = name
        self.words = words
        self.percentage_missing_words = percentage_missing_words
        if os.path.exists('missing_keys.pkl'):
            with open('missing_keys.pkl', 'rb') as file:
                self.w_missing_words = pickle.load(file)
        else:
            self.w_missing_words = []

    def form_sentence(self, count: int):
        words = []
        sentence = []
        for _ in range(0, count):
            if len(words) == 0:
                words = self.words.copy()
            word = words[random.randint(0, len(words) - 1)]
            sentence.append(word.lower())
            words.remove(word)
        return " ".join(sentence if not self.w_missing_words else self.select_newwords(sentence))

    def select_newwords(self, array_words):
        size_sentence = len(array_words)
        old_words_index = int((1 - self.percentage_missing_words) * size_sentence) 
        missing_words = []
        new_words = array_words[0:old_words_index]
        while(True):
            if len(missing_words) >= len(array_words) - old_words_index:
                break
            word_sel = self.words[random.randint(0, len(self.words)-1)]
            set_word = set(word_sel)

            keys, weights = zip(*self.w_missing_words.items())
            total = sum(weights)
            p_k = [i/total for i in weights]

            sel_missed_letter = np.random.choice(keys, 1, p=p_k)[0]
            if sel_missed_letter in set_word:
                missing_words.append(word_sel.lower())

        new_words += missing_words
        random.shuffle(new_words)
        return new_words


    @staticmethod
    def list_dictionaries():
        files = os.listdir(Dictionary.dictionaries_path)
        result = []
        for file in files:
            if file.endswith(".json"):
                result.append(file[:-5])

        return result
    
    @staticmethod
    def load_dictionary(name: str):
        if name in dictionaries_cache:
            return dictionaries_cache[name]

        path = os.path.join(
            Dictionary.dictionaries_path,
            name + ".json",
        )
        if not os.path.exists(path):
            raise DictionaryError("This dictionary does not exist locally")
        
        f = open(path, "r")
        d = json.loads(f.read())
        f.close()
        
        dictionary = Dictionary(path, name, d["words"], percentage_missing_words=0.5)
        dictionaries_cache[name] = dictionary
        return dictionary
