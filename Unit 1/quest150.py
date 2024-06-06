def longest_name(file_path):
    """
    Finds and prints the longest name (line) in a given file.

    Args:
        file_path: Path to the file containing names (one name per line).
    """
    print(max(line.strip() for line in open(file_path)))


def sum_len(file_path):
    """
    Calculates and prints the total combined length of all names (lines) in a file.

    Args:
        file_path: Path to the file containing names.
    """
    print(sum(len(line.strip()) for line in open(file_path)))


def shortest_name(file_path):
    """
    Finds and prints the shortest name(s) (lines) in a file.

    Args:
        file_path: Path to the file containing names.
    """
    shortest_word_length = min(len(word.strip()) for word in open(file_path))
    print(*[word for word in open(file_path) if len(word.strip()) == shortest_word_length])


def print_line_lengths(file_path, output_file='line_lengths.txt'):
    """
    Writes the length of each line in a file to a new output file.

    Args:
        file_path: Path to the input file.
        output_file: Name of the output file.
    """
    with open(file_path, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write('\n'.join(str(len(line.rstrip())) for line in infile))


def word_len(file_path):
    """
    Finds and prints names (lines) of a specified length from a file.

    Args:
        file_path: Path to the file containing names.
    """
    user_len = int(input("please enter len: ")) 
    print(*[word for word in open(file_path) if len(word.strip()) == user_len])


word_len('/name.txt')
