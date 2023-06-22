import PySimpleGUI as sg
import datetime
import subprocess
import os
import webbrowser

sg.theme('Dark')

layout = [
    [sg.Menu([['File', ['New', 'Open', 'Save', 'Save as', '---', 'Exit']],
              ['Run', ['Run script']]], key='_MENU_')],
    [sg.Multiline(size=(80, 25), font=('Courier', 12), key='_BODY_', enable_events=True, autoscroll=True)]
]

window = sg.Window('Simnote Version 0.1 -', layout)

filename = None

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Open':
        filename = sg.popup_get_file('Open', no_window=True)
        if filename:
            with open(filename, 'r') as f:
                window['_BODY_'].update(f.read())
                window.set_title('Simnote Version 0.1 - ' + filename)
    elif event == 'New':
        filename = None
        window['_BODY_'].update('')
        window.set_title('Simnote Version 0.1 -')
    elif event in ('Save', 'Save as'):
        if not filename or event == 'Save as':
            filename = sg.popup_get_file('Save', save_as=True, no_window=True)
        if filename:
            with open(filename, 'w') as f:
                f.write(values['_BODY_'])
                window.set_title('Simnote Version 0.1 - ' + filename)
    elif event == 'Copy':
        window['_BODY_'].copy()
    elif event == 'Paste':
        window['_BODY_'].paste()
    elif event == '<F11>':
        now = datetime.datetime.now()
        cursor_index = window['_BODY_'].Widget.index('insert')
        window['_BODY_'].Widget.insert(cursor_index, now.strftime('%d-%m-%Y'))
    elif event == 'Run script':
        if filename:
            file_ext = os.path.splitext(filename)[1]
            if file_ext == '.sh' or file_ext == '.bash':
                subprocess.Popen(['bash', filename])
            elif file_ext == '.py':
                subprocess.Popen(['python', filename])
            elif file_ext == '.html':
                webbrowser.open(filename)
            else:
                sg.popup_error('Unsupported file type. Only .sh, .bash, .py, and .html files are supported.')
        else:
            sg.popup_error('Please open a file first.')

window.close()
