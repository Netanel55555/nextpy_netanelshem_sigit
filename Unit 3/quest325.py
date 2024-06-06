def read_file(file_name):
    try:
        f = open(file_name)
    except FileNotFoundError as e:
        print(e)
        content = "__NO_SUCH_FILE__"

    else:
        content = f.read()

    finally:

        return f"__CONTENT_START__\n{content}\n__CONTENT_END__"

print(read_file("/name.txt"))