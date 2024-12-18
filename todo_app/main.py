from functions  import get_todos, write_todos
while True:
    arg = input("Please insert add,show,edit,complete or exit: ")
    print("\n")
    if arg.startswith("add"):
        if len(arg)>len('add')+1:
            added = arg[len('add')+1:] + '\n'
        else:
            added = input("Please insert the element you want to add: ") + "\n"

        todos = get_todos()

        todos.append(added)

        write_todos(todos)

    elif arg.startswith("show"):

        todos = get_todos()
        
        for i,v in enumerate(todos):
            print(f"{i + 1} - {v.strip('\n')}")

    elif arg.startswith("edit"):
        try:
            index = int(arg[5:])

            edited = input("Please insert the value you want to replace the original element with: ")

            
            todos = get_todos()

            todos[index-1] = edited + '\n'

            write_todos(todos)

        except IndexError:
            print("Please enter a value that is in range.")
            continue
         
    elif arg.startswith("complete"):
        t=input("Please insert the number of the element or the name you want to delete: ")
        todos = get_todos()

        if t in "123456789":
            m = todos.pop(int(t)-1)
            print(f"You removed the todos list element called: {m}")
        else:
            t = t + '\n'
            todos.remove(t)
            print(f"You removed the todos list element called: {t}")
        
        write_todos(todos)

    elif 'exit' in arg.lower():
        break
    else:
        print("Please insert a valid command!")


