# Color Picker

This is a GUI version to pick colors

The dial can be adjusted to change color
The same functionality can be achieved using spinbox aswell

Every time its loaded, it generates a random color

- To run this, download/clone the folder
- Open command prompt/terminal
- run main.py using command `python main.py`

To convert `.ui` file to `.py` use the command `pyuic5 input.ui -o output.py`

To use it as `.exe` file, install pyinstaller using command `pip install pyinstaller`
Open cmd/terminal and go to the folder where the program is present and use the command `pyinstaller --onefile -w main.py`
Now the `.exe` file can be used to heart's content
