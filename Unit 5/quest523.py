from itertools import combinations

Bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]


def main():
    combs_list = []
    for index in range(0, len(Bills)):
        current_comb = combinations(Bills, len(Bills) - index)
        combs_list.extend(set(current_comb))

    options = 0
    for current_comb in combs_list:
        if sum(current_comb) == 100:
            options += 1

    print(f'Number of combinations: {options}')


if __name__ == "__main__":
    main()
