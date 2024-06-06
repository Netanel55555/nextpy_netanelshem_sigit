

def StopIteration_trigger():
    my_list = [1, 2, 3]
    my_iterator = iter(my_list)

    while True:
        item = next(my_iterator)
        print(item)


def ZeroDivisionError_trigger():
    print(7/0)

def AssertionError_trigger():
    x = 10
    assert x == 9, print("bop")


def trigger_import_error():
    import NumPy

def KeyError_trigger():
    favorite_colors = {
        "Alice": "blue",
        "Bob": "green",
        "Carol": "red"
    }

    print(favorite_colors["netanel"])

def SyntaxError_trigger():
    print("hey"

def IndentationError_trigger(x):

    print("hey")
     print("bop")

def TypeError_trigger():
    print(4 + '3')



