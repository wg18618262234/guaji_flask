from player import db
import json


# 创建模型对象
class Player_info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    hp = db.Column(db.String(100))
    power = db.Column(db.String(100))

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def __repr__(self):
        return json.dumps({'name':self.name,'hp':self.hp,'power':self.power})