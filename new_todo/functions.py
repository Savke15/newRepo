def get_todos():
    with open("todo_app/files/newfile.txt","r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todo):
    with open("todo_app/files/newfile.txt", "w") as file:
            file.writelines(todo)
