from random import randint

from flask import render_template, request

from app import app


@app.route('/', methods=["GET", "POST"])
def start_page_of_site():
    number = 0
    if request.method == 'POST':
        range = int(request.form['range'])
        try:
            number = randint(1,range)
        except ValueError:
            number = "Число должно быть отличным от нуля!"
    return render_template('relative.html', number=number), 200
