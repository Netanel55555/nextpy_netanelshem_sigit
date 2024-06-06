class BigThing:

    def __init__(self, data):
        self._data = data

    def size(self):
        if isinstance(self._data, int):
            print(self._data)
        else:
            print(len(self._data))


class BigCat(BigThing):

    def __init__(self, data, weight):
        super().__init__(data)
        self._weight = weight

    def size(self):
        if self._weight > 15:
            if self._weight > 20:
                print("Very Fat")
            else:
                print("Fat")
        else:
            print("Ok")


def main():
    cutie = BigCat("mitzy", 22)
    cutie.size()


main()
