import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do:")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")
print("New message")
print("New")
window = sg.Window("My To-Do App",layout=[[label],[input_box, add_button]])
window.read()
print("Okay")
window.close()

