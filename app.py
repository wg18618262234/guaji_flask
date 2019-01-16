from flask import Flask, render_template, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def errorhandler(error):
    return render_template('page_not_found.html'), 404


# 玩家信息添加
@app.route('/player/info/add/', methods=['GET', 'POST'])
def player_info_add():
    if request.method == 'POST':
        from models import Player_info
        Pname = str(request.form.get('Pname'))
        Php = str(request.form.get('Php'))
        Ppower = str(request.form.get('Ppower'))
        db.session.add(Player_info(Pname, Php, Ppower))
        return render_template('player_info_add.html')
    else:
        return render_template('player_info_add.html')


# 玩家信息根据Pid查询
@app.route('/player/info/show/', methods=['GET', 'POST'])
def player_info_show():
    from models import Player_info
    if request.method == 'POST':
        Pid = str(request.form.get('Pid'))
        player_datas = db.session.query(Player_info).filter_by(id=Pid).all()
        result = []
        for player_data in player_datas:
            result.append(player_data.to_json())
        return jsonify(result)
    else:
        Pid = str(request.args.get('Pid'))
        player_datas = db.session.query(Player_info).filter_by(id=Pid).all()
        result = []
        for player_data in player_datas:
            result.append(player_data.to_json())
        return jsonify(result)


# 怪物信息添加
@app.route('/monster/info/add/', methods=['GET', 'POST'])
def monster_info_add():
    if request.method == 'POST':
        from models import Monster_info
        Pname = str(request.form.get('Pname'))
        Php = str(request.form.get('Php'))
        Ppower = str(request.form.get('Ppower'))
        db.session.add(Monster_info(Pname, Php, Ppower))
        return render_template('monster_info_add.html')
    else:
        return render_template('monster_info_add.html')


# 怪物信息根据Pid查询
@app.route('/monster/info/show/', methods=['GET', 'POST'])
def monster_info_show():
    from models import Monster_info
    if request.method == 'POST':
        Pid = str(request.form.get('Pid'))
        player_datas = db.session.query(Monster_info).filter_by(id=Pid).all()
        result = []
        for player_data in player_datas:
            result.append(player_data.to_json())
        return jsonify(result)
    else:
        Pid = str(request.args.get('Pid'))
        player_datas = db.session.query(Monster_info).filter_by(id=Pid).all()
        result = []
        for player_data in player_datas:
            result.append(player_data.to_json())
        return jsonify(result)


if __name__ == '__main__':
    app.run()
