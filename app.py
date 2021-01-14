from commands import commands_dict


def parse(command):
    """
  Takes the command as input and returns the command name and args
  """
    cmd_list = command.split()
    cmd_type = cmd_list[0]
    if cmd_type == 'help' or cmd_type == 'quit':
        return cmd_type, []
    elif cmd_type == 'todo':
        cmd_name = cmd_list[1]
        if cmd_name in ['add', 'del', 'done', 'report', 'help', 'ls', 'quit']:
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid', []
    else:
        return 'invalid', []


def main():
    print('Started the To-Do Application ')
    current_list = []
    while 1:
        # take the command as input from the user
        command = input('$ ')
        command_name, command_args = parse(command)
        # print(command_name, command_args)
        if command_name == 'quit' or command_name == 'todo quit':
            break
        elif command_name == 'help' or command_name == 'todo help':
            with open('help.txt', 'r') as help_file:
                print(help_file.read())
        elif command_name == 'invalid':
            print('Please enter a valid command, use help command to display all!')
        elif command.split()[0] == 'todo':
            # todo type of command
            command_args.insert(0, current_list)
            commands_dict[command_name](command_args)
        else:
            commands_dict[command_name](command_args)


if __name__ == '__main__':
    main()
