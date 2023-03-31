FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Example of a description of a function
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local1:
        file_local1.writelines(todos_arg)


if __name__ == "__name__":
    print("Hello")
    print(get_todos())
