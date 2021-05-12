try:
    from sql_helper import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String, UnicodeText

class Global(BASE):
    __tablename__ = "global"
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value):
        self.variable = str(variable)
        self.value = value

Global.__table__.create(checkfirst=True)

def getglobal(variable):
    try:
        return (
            SESSION.query(Global)
            .filter(Global.variable == str(variable))
            .first()
            .value
        )
    except BaseException:
        return None
    finally:
        SESSION.close()

def addglobal(variable):
    if SESSION.query(Global).filter(Global.variable == str(variable)).one_or_none():
        delglobal(variable)
    adder = Global.(str(variable), value)
    SESSION.add(adder)
    SESSION.commit()

def delglobal(variable):
    rem = (
        SESSION.query(Global)
        .filter(Global.variable == str(variable))
        .delete(synchronize_session="fetch")
    )
    if rem:
        SESSION.commit()    
