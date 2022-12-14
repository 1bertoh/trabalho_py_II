from flask import Flask
import os

app = Flask(__name__)

root_path = os.path.abspath(".\\")

for entry in os.scandir(f"{root_path}\\flask\\views"):
    if entry.is_file():
        classname = entry.name[:-3]
        string = f'from views.{classname} import {classname}'
        exec(string)
        string = f'{classname}.register(app)'
        exec(string)

if __name__ == '__main__':
    app.run(debug=True)