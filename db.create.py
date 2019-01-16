from models import db

# 1.创建表
db.create_all()

# # 2.增加记录
# admin = Player_info(player_name='admin', player_hp='1000000', player_power='1')
# guest = Player_info(player_name='guest', player_hp='1000', player_power='1000000')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()
# # 3.查询记录，注意查询返回对象，如果查询不到返回None
# Player_info.query.all()  # 查询所有
# Player_info.query.filter_by(player_name='admin').first()  # 条件查询
# Player_info.query.order_by(Player_info.id).all()  # 排序查询
# Player_info.query.limit(1).all()  # 查询1条
# Player_info.query.get(id=1)  # 精确查询
# # 4,删除
# player_logic = Player_info.query.get(id=1)
# db.session.delete(player_logic)
# db.session.commit()
