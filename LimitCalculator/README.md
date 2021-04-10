# Limit Calculator

Calculating Target price and Stop Loss in trading is very important and could be life changer too.
But when it comes to intraday trading, you might not have enough time to calculate in certain situations.
At those times, this software shines by just entering the current `price` of the stock and then
`quantity` which is default to 1 if nothing is entered.


[!Screenshot](limitCalc.png)
![alt text](https://github.com/Anudeep-K2001/mini-projects/edit/main/LimitCalculator/limitCalc.png?raw=true)



- To run this, download/clone the folder
- Open command prompt/terminal
- run main.py using command `python main.py`

To convert `.ui` file to `.py` use the command `pyuic5 input.ui -o output.py`

To use it as `.exe` file, install pyinstaller using command `pip install pyinstaller`
Open cmd/terminal and go to the folder where the program is present and use the command `pyinstaller --onefile -w main.py`
Now in the dist folder you can find the `.exe` file

