from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


# 链接是需要指定要用到的MySQL数据库
engine = create_engine('mysql+pymysql://root:wangmingdong1225@localhost:3306/py3_sqlalchemy?charset=utf8', echo=True)
Base = declarative_base()  # 生成SQLORM基类


class User(Base):

    # 对应MySQL中数据表的名字
    __tablename__ = 'users'

    # 创建字段
    id = Column(Integer, primary_key=True)  #users表中的id字段(主键)
    username = Column(String(64), nullable=False, index=True)  # uers表中的username字段
    password = Column(String(64), nullable=False)  # users表中的password字段
    email = Column(String(64), nullable=False, index=True)  # users表中的email字段(有索引)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

# 创建userinfo表（所有表结构）
# Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类
# 创建session对象
session = DBSession()  # 生成链接数据库的实例
new_user1 = User(id='2', username='python-teacher2', password="112233", email="laoyan@163.com")
new_user2 = User(id='3', username='python-teacher3', password="654321", email="laoma@163.com")
new_user3 = User(id='4', username='python-teacher4', password="789012", email="laoye@163.com")
session.add_all([new_user1, new_user2, new_user3])
session.commit()
session.close()