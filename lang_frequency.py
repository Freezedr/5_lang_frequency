from collections import Counter
import re
import sys

def load_data(filepath):
    with open(filepath) as f:
        return f.read()

def get_most_frequent_words(text):
    c = Counter(re.split("\W+", text))
    return c.most_common(10)


if __name__ == '__main__':
    filepath = sys.argv[1]
    text = load_data(filepath)
    print(get_most_frequent_words(text))
