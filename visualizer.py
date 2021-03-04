import redis
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

client = redis.Redis(host="127.0.0.1", port=6379,
                     charset="utf-8", decode_responses=True)

array = client.lrange("messages", 0, -1)

min_letter_length = 3
min_occurrences = 20


def parse_data(array):

    collection = []

    for sentence in array:
        words = sentence.split()

        if words:
            collection = collection + words

    return collection


def generate_graph():
    data = parse_data(array)

    counter = Counter(data)

    x = []
    y = []

    # count appearences of strings

    for ele in counter:
        if counter[ele] > min_occurrences and len(ele) > min_occurrences:
            print(len(ele))
            x.append(ele)
            y.append(counter[ele])

    # actually generate graph here now

    plot = plt.barh(x, y, 2)
    plt.xlabel('Messages')
    plt.ylabel('Occurrences')
    plt.title('Discord activity')

  #  plot.set_xticklabels(df.index, rotation=45,
   #                      rotation_mode='anchor', ha='right')

    plt.show()


def search(value):
    matching = [s for s in array if value in s]

    print(matching)
    print("Occurrences: " + str(len(matching)))


generate_graph()
