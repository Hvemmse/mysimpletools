import PySimpleGUI as sg

def save_to_file(tasks):
    with open('todo.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load_from_file():
    tasks = []
    try:
        with open('todo.txt', 'r') as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        pass
    return tasks

def main():
    tasks = load_from_file()

    layout = [
        [sg.Text('Task:'), sg.InputText(key='task_input'), sg.Button('Add')],
        [sg.Listbox(values=tasks, key='task_list', size=(40, 10))],
        [sg.Button('Remove'), sg.Button('Save'), sg.Button('Exit')]
    ]

    window = sg.Window('To-Do List', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Add':
            task = values['task_input']
            tasks.append(task)
            window['task_list'].update(values=tasks)

        if event == 'Remove':
            selected_tasks = values['task_list']
            tasks = [task for task in tasks if task not in selected_tasks]
            window['task_list'].update(values=tasks)

        if event == 'Save':
            save_to_file(tasks)
            sg.popup('To-do list saved to todo.txt')

    window.close()

if __name__ == '__main__':
    main()

