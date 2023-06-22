import PySimpleGUI as sg


def generate_html(title, slogan, contact_info, page, theme):
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body class="{theme}">
        <div id="menu">
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="service.html">Business Service</a></li>
            </ul>
        </div>
        <h1>{title}</h1>
        <p>{slogan}</p>
        <p>Contact: {contact_info}</p>
    </body>
    </html>
    '''

    filename = ''
    if page == 'index':
        filename = 'index.html'
    elif page == 'about':
        filename = 'about.html'
    elif page == 'service':
        filename = 'service.html'

    with open(filename, 'w') as file:
        file.write(html_template)
    print(f'{filename} has been saved.')


def generate_css(theme):
    css_template = f'''
    /* CSS Styles */
    body.light {{
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
        padding: 20px;
    }}

    body.dark {{
        font-family: Arial, sans-serif;
        background-color: #333333;
        color: #ffffff;
        padding: 20px;
    }}

    h1 {{
        color: #333333;
    }}

    p {{
        color: #666666;
    }}

    #menu {{
        background-color: #333333;
        padding: 10px;
    }}

    #menu ul {{
        list-style-type: none;
        margin: 0;
        padding: 0;
    }}

    #menu ul li {{
        display: inline;
    }}

    #menu ul li a {{
        color: #ffffff;
        text-decoration: none;
        margin-right: 10px;
    }}
    '''
    return css_template


def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f'{filename} has been saved.')


def main():
    sg.theme('LightGrey1')

    layout = [
        [sg.Text('Title:'), sg.InputText(key='-TITLE-')],
        [sg.Text('Slogan:'), sg.InputText(key='-SLOGAN-')],
        [sg.Text('Contact Info:'), sg.InputText(key='-CONTACT-')],
        [sg.Text('Select Page:'), sg.Combo(['index', 'about', 'service'], key='-PAGE-')],
        [sg.Text('Select Theme:')],
        [sg.Radio('Light', 'THEME', default=True, key='-LIGHT-'),
         sg.Radio('Dark', 'THEME', key='-DARK-')],
        [sg.Button('Generate HTML')]
    ]

    window = sg.Window('HTML Generator', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Generate HTML':
            title = values['-TITLE-']
            slogan = values['-SLOGAN-']
            contact_info = values['-CONTACT-']
            page = values['-PAGE-']
            theme = 'light' if values['-LIGHT-'] else 'dark'

            html_content = generate_html(title, slogan, contact_info, page, theme)
            css_content = generate_css(theme)

            save_file('styles.css', css_content)
            generate_html(title, slogan, contact_info, 'index', theme)
            generate_html(title, slogan, contact_info, 'about', theme)
            generate_html(title, slogan, contact_info, 'service', theme)

    window.close()


if __name__ == '__main__':
    main()
