from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义Actor对象:
class Actor(Base):
    # 表的名字:
    __tablename__ = 'x_actor'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    actor_name = Column(String(255))
    actor_img = Column(String(255))
    actor_link = Column(String(255))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/xlov')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
actor = session.query(Actor).filter(Actor.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(actor))
print('actor_name:', actor.actor_name)
# 关闭Session:
session.close()


# session = DBSession()

# new_actor = Actor( actor_name='test name', actor_img='test actor img', actor_link='test link')
# session.add(new_actor)

# session.commit()
# session.close()


session = DBSession()
# 更新，返回影响行数， 删除类似，调用delete()
# res = session.query(Actor).filter(Actor.actor_name == 'test name').update({"actor_link":"updated link"})
res = session.query(Actor).filter(Actor.actor_name == 'test name').delete()
print(res)

session.commit()
session.close()