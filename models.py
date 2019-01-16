from app import db


# 创建玩家信息模型对象
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
        return {'name': self.name, 'hp': self.hp, 'power': self.power}

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


# 创建小怪信息模型对象
class Monster_info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    hp = db.Column(db.String(100))
    power = db.Column(db.String(100))

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def __repr__(self):
        return {'name': self.name, 'hp': self.hp, 'power': self.power}

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
