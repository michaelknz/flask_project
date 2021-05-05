from flask import render_template
import keyboard


class Drop_Test:
    def __init__(self):
        pass

    def Drop(self):
        return render_template('drop/drop.html')
