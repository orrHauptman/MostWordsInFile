from sys import argv
from collections import Counter

num : int = int(argv[0])

list_of_words: list[str] = []

with open("Text.txt" , "r" ) as f :
    list_of_words = f.read().split(" ")

appearances: dict [str , int] = Counter(list_of_words)

