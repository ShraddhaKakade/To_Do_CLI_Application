from datetime import datetime, date

list1 = []
complete = 0
list_count = len(list1)


def add_item(args):
  """
  Adds a todo item to the todo list
  """
  global list1
  title = args[1:250]
  new_todo = {
    'title': title,
    'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    'completed': False
  }
  list1.append(new_todo)
  title1 = ' '.join(map(str, title))
  print(f'Added todo : {title1}')
  global list_count
  list_count = list_count + 1


def show_items(args):
  """
  Prints all the todo items in the currently chosen todo list
  """
  global list1
  if len(list1) == 0:
    print('No todos in the list :)')
  else:
    for index, todo_item in enumerate(list1):
      print(index + 1, ' '.join(map(str, todo_item['title'])))
      if todo_item['completed']:
        global complete
        complete += 1


def remove_item(args):
  """
  Remove a todo item
  """
  global list1
  item_id = int(args[1])
  if item_id > len(list1):
    print("Invalid !")
  elif item_id <= 0:
    print("Invalid !")
  else:
    list1.pop(item_id - 1)
    print(f'Deleted todo : {item_id}')
    global list_count
    list_count = list_count-1


def complete_item(args):
  """
  Mark a todo item as completed
  """
  global list1, complete, list_count
  item_id = int(args[1])
  if item_id > len(list1):
    print("Invalid !")
  elif item_id <= 0:
    print("Invalid !")
  else:
    list1[item_id - 1]['completed'] = True
    list1.pop(item_id - 1)
    print(f'Done todo : {item_id}')
    complete = complete - 1
    list_count = list_count-1


def show_report(args):
  """
  Displays completed and pending todos
  """
  global list_count, complete
  print(f'{date.today()} Completed : {-complete} Pending : {list_count}')

