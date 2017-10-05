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
    word_amount = 10
    return c.most_common(word_amount)


if __name__ == '__main__':
    filepath_arg_position = 1
    filepath = sys.argv[filepath_arg_position]
    if filepath:
        text = load_data(filepath)
        if text:
            print(get_most_frequent_words(text))
    else:
        print("Launch again with file path")
