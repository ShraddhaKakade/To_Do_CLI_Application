import commands.todos

commands_dict = {
  'add': todos.add_item,
  'ls': todos.show_items,
  'del': todos.remove_item,
  'done': todos.complete_item,
  'report': todos.show_report
}