from sys import argv
from collections import Counter

N : int = int(argv[1])

list_of_words: list[str] = []

with open("Text.txt" , "r" ) as f :
    list_of_words = f.read().split()

appearances: dict [str , int] = Counter(list_of_words)

descending_list : list[str] = sorted(appearances.keys() , reverse=True ,key = lambda key : appearances[key])

placement: int = 1
count_times: int = 0

while count_times < N and count_times < len(descending_list):
    current_word: str = descending_list[count_times]
    print(f"{placement} - word \"{current_word}\" {appearances[current_word]} times")
    count_times += 1
    placement += 1

if count_times == len(descending_list) and count_times != N:
    print("No more words")

