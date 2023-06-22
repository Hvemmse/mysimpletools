import PySimpleGUI as sg

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except (SyntaxError, ZeroDivisionError):
        return "Error"

# Define the dark theme
sg.theme('Dark2')

# Create the GUI layout
layout = [
    [sg.Input(size=(25, 1), key='-DISPLAY-', justification='right', background_color='#333333', text_color='#ffffff')],
    [sg.Button('7', button_color=('#333333', '#ffffff')), sg.Button('8', button_color=('#333333', '#ffffff')),
     sg.Button('9', button_color=('#333333', '#ffffff')), sg.Button('/', button_color=('#333333', '#ffffff'))],
    [sg.Button('4', button_color=('#333333', '#ffffff')), sg.Button('5', button_color=('#333333', '#ffffff')),
     sg.Button('6', button_color=('#333333', '#ffffff')), sg.Button('*', button_color=('#333333', '#ffffff'))],
    [sg.Button('1', button_color=('#333333', '#ffffff')), sg.Button('2', button_color=('#333333', '#ffffff')),
     sg.Button('3', button_color=('#333333', '#ffffff')), sg.Button('-', button_color=('#333333', '#ffffff'))],
    [sg.Button('0', button_color=('#333333', '#ffffff')), sg.Button('.', button_color=('#333333', '#ffffff')),
     sg.Button('C', button_color=('#333333', '#ffffff')), sg.Button('+', button_color=('#333333', '#ffffff'))],
    [sg.Button('=', size=(20, 1), button_color=('#333333', '#ffffff'))]
]

# Create the window
window = sg.Window('Calculator', layout, return_keyboard_events=True, element_justification='center')

expression = ''

# Event loop to process events and get user input
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # Concatenate the button pressed to the expression
    if event in '1234567890.+-*/':
        expression += event
        window['-DISPLAY-'].update(expression)

    # Clear the expression
    elif event == 'C':
        expression = ''
        window['-DISPLAY-'].update('')

    # Evaluate the expression
    elif event == '=':
        result = evaluate_expression(expression)
        window['-DISPLAY-'].update(result)
        expression = result

# Close the window
window.close()
