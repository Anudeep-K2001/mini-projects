# Limit Calculator

Calculating Target price and Stop Loss in trading is very important and could be life changer too.
But when it comes to intraday trading, you might not have enough time to calculate in certain situations.
At those times, this software shines by just entering the current `price` of the stock and then
`quantity` which is default to 1 if nothing is entered.


[Limit Calculator image](limitCalc.png?raw=true)

* `Target` is the Target price
* `Stop Loss` is the stop loss amount
* `Total Value` is the product of price and quantity
* The value above buy is the difference between target and price
* The vale above sell is the difference between stop loss and price
* The Green Value is the Profit that could be benefited if trade goes your way
* The Red value is the Loss that could occur if trade goes wrong

- To run this, download/clone the folder
- Open command prompt/terminal
- run main.py using command `python main.py`

To convert `.ui` file to `.py` use the command `pyuic5 input.ui -o output.py`

To use it as `.exe` file, install pyinstaller using command `pip install pyinstaller`
Open cmd/terminal and go to the folder where the program is present and use the command `pyinstaller --onefile -w main.py`
Now in the dist folder you can find the `.exe` file

