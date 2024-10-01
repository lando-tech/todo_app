import os
import json
import curses


class Todo:

    def __init__(self) -> None:
        self.todo_dict = {
                "Tasks": [],
                }
    def add_task(self):
        task = input("Please enter a task: ")
        if os.path.isfile('todo.json'):
            task_id = self.get_todo_list_length() + 1
            entry = (task_id, task)
            self.todo_dict['Tasks'].append(entry)
            self.append_to_file(entry)
        else:
            entry = (1, task)
            self.todo_dict['Tasks'].append(entry)
            self.write_to_file(self.todo_dict)

    def get_todo_list_length(self):
        with open('todo.json', 'r', encoding='utf-8') as length:
            todo_length = json.load(length)
            return len(todo_length['Tasks'])

    def delete_task(self):
        print("Please select a task to delete:\n")
        self.view_tasks()
        task_choice = input('\n: ')
        for i in range(len(self.view_tasks())):
            if i == task_choice:
                self.view_tasks().pop(self.view_tasks()[i])

    def complete_task(self):
        pass

    def view_tasks(self):
        with open('todo.json', 'r', encoding='utf-8') as view:
            tasks = json.load(view)

            for i in tasks['Tasks']:
                print(f'\t{i}')

            return tasks['Tasks']

    def write_to_file(self, todo_dict):
        with open('todo.json', 'w', encoding='utf-8') as new_entry:
            json.dump(fp=new_entry, obj=todo_dict, indent=4)


    def append_to_file(self, entry):
        with open('todo.json', 'r', encoding='utf-8') as new_entry:
            data = json.load(new_entry)
            
            data['Tasks'].append(entry)

            with open('todo.json', 'w', encoding='utf-8') as updated_entry:
                json.dump(fp=updated_entry, obj=data, indent=4)

