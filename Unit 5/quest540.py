def check_id_valid(id_number):
    id_str = str(id_number).zfill(9)
    total = 0
    for i, digit in enumerate(id_str):
        num = int(digit) * (1 if i % 2 == 0 else 2)
        total += num if num < 10 else num - 9
    return total % 10 == 0


class IDIterator:
    def __init__(self, id_):
        self.id_ = id_
        self.current_id = id_

    def __iter__(self):
        return self

    def __next__(self):
        self.current_id += 1
        while self.current_id <= 999999999:
            if check_id_valid(self.current_id):
                return self.current_id
            self.current_id += 1
        raise StopIteration


def id_generator(id_):
    current_id = id_
    while current_id <= 999999999:
        current_id += 1
        if check_id_valid(current_id):
            yield current_id


def main():
    user_id = int(input("Enter ID: "))
    method = input("Generator or Iterator? (gen/it)? ").strip().lower()

    if method == "it":
        iterator = IDIterator(user_id)
        for i in range(10):
            print(next(iterator))
    elif method == "gen":
        generator = id_generator(user_id)
        for i in range(10):
            print(next(generator))
    else:
        print("Invalid method. Please enter 'gen' or 'it'.")


if __name__ == '__main__':
    main()
