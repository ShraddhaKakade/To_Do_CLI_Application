### **[A] "commands" directory :**

### **1) __init__.py**
----> This python file contains a dictionary of **_'todo_commands':'function_objects'_** key-value pairs

### **2) todos.py**
----> This python file contains all the required functions to operate the commands in CLI . 
----> The functions are as follows :

##### **a.** **_add_item()_** :- This function adds todos to the todo list - **_'list1'_**
##### **b.** **_show_items()_** :- This function displays list of all todos
##### **c.** **_remove_item()_** :- This function deletes choosen todo from the list
##### **d.** **_complete_item()_** :- This function marks choosen todo as done and removes it from list
##### **e.** **_show_report()_** :- This function displays the number of completed and pending todos

### **[B] app.py**
----> This python file is the main file of the project which is executed on command line

### **[C] help.txt**
----> This is a text file which displays command line instructions when _todo help_ or _help_ command is entered on command line window
