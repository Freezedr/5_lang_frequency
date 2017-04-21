from collections import Counter
import re
import sys

word_amount = 10
filepath_arg_position = 1

def load_data(filepath):
    with open(filepath) as f:
        return f.read()

def get_most_frequent_words(text):
    c = Counter(re.split("\W+", text))
    return c.most_common(word_amount)

if __name__ == '__main__':
    filepath = sys.argv[filepath_arg_position]
    if filepath:
        text = load_data(filepath)
        print(get_most_frequent_words(text))
    else:
        print("Launch again with file path")
