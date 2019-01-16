from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/player/info/add', methods=['GET', 'POST'])
def player_info_get():
    if request.method == 'POST':
        from models import Player_info
        Pname = str(request.form.get('Pname'))
        Php = str(request.form.get('Php'))
        Ppower = str(request.form.get('Ppower'))
        db.session.add(Player_info(Pname, Php, Ppower))
        return render_template('player_info_add.html')
    else:
        return render_template('player_info_add.html')


@app.route('/player/info/show', methods=['GET', 'POST'])
def player_info_show():
    if request.method == 'POST':
        from models import Player_info
        Pid = str(request.form.get('Pid'))
        player_data=db.session.query(Player_info).filter_by(id=Pid).all()
        return str(player_data)


if __name__ == '__main__':
    app.run()
