from typing import List
import json
import os
import random

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

    def __init__(self, path: str, name: str, words: List[str]):
        self.path = path
        self.name = name
        self.words = words

    def form_sentence(self, count: int):
        words = []
        sentence = []

        for _ in range(0, count):
            if len(words) == 0:
                words = self.words.copy()

            word = words[random.randint(0, len(words) - 1)]
            sentence.append(word.lower())
            words.remove(word)

        return " ".join(sentence)
            

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
        
        dictionary = Dictionary(path, name, d["words"])
        dictionaries_cache[name] = dictionary
        return dictionary
