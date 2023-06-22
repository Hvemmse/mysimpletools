import PySimpleGUI as sg
import os
import webbrowser

# Define the layout of the GUI
layout = [
    [sg.Text("Select a directory:")],
    [sg.Input(size=(50, 1), key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Button("Show Files"), sg.Button("Cancel")],
    [sg.Text("Files in the selected directory:")],
    [sg.Listbox([], size=(70, 20), key="-FILES-", enable_events=True)]
]

# Create the window
window = sg.Window("File Browser", layout)

# Event loop to process events and get input from the user
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    if event == "Show Files":
        folder_path = values["-FOLDER-"]
        if folder_path:
            # Fetch all files and folders in the directory
            items = os.listdir(folder_path)
            # Add "." and ".." to the list
            items.insert(0, ".")
            items.insert(1, "..")

            # Update the listbox with the items
            window["-FILES-"].update(values=items)

    if event == "-FILES-":
        selection = values["-FILES-"][0]
        if selection == "..":
            # Go one step up in the directory tree
            folder_path = os.path.dirname(values["-FOLDER-"])
            window["-FOLDER-"].update(folder_path)
            items = os.listdir(folder_path)
            items.insert(0, ".")
            items.insert(1, "..")
        else:
            item_path = os.path.join(values["-FOLDER-"], selection)
            if os.path.isfile(item_path):
                # Open the selected file
                webbrowser.open(item_path)
            elif os.path.isdir(item_path):
                # Fetch all files and folders in the selected folder
                items = os.listdir(item_path)
                items.insert(0, ".")
                items.insert(1, "..")
                # Update the listbox with the items
                window["-FILES-"].update(values=items)
                # Update the folder input field with the new directory path
                window["-FOLDER-"].update(item_path)

# Close the window
window.close()

