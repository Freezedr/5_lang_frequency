from collections import Counter
import re
import sys

def load_data(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        print("File not exist, try again")
        return None


def get_most_frequent_words(text):
    c = Counter(re.split("\W+", text))
    WORD_AMOUNT = 10
    return c.most_common(WORD_AMOUNT)


if __name__ == '__main__':
    FILEPATH_ARG_POSITION = 1
    filepath = sys.argv[FILEPATH_ARG_POSITION]
    if filepath:
        text = load_data(filepath)
        if text:
            print(get_most_frequent_words(text))
    else:
        print("Launch again with file path")
