from datetime import datetime

from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from utilities.hash_controler import hash_password
from settings.configs import SQLITE_DB_PATH

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    position_id = Column(Integer, ForeignKey('position.id'), nullable=True)
    address = Column(String, nullable=True)
    manager_id = Column(Integer, ForeignKey('employee.id'), nullable=True)
    image = Column(String, nullable=True)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    
    position = relationship("Position", back_populates="employees")
    manager = relationship("Employee", remote_side=[id], back_populates="subordinates", foreign_keys=[manager_id])
    subordinates = relationship("Employee", back_populates="manager", cascade="all, delete-orphan", foreign_keys=[manager_id])
    state = relationship("State", back_populates="employees")
    managed_departments = relationship("Department", back_populates="manager", foreign_keys='Department.manager_id')

class Position(Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=True)
    details = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    
    employees = relationship("Employee", back_populates="position")

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=True)
    manager_id = Column(Integer, ForeignKey('employee.id'), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    
    manager = relationship("Employee", back_populates="managed_departments")
    
class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    
    employees = relationship("Employee", back_populates="state")

# Database initialization function
def init_db():
    engine = create_engine(f'sqlite:///{SQLITE_DB_PATH}', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    
    try:
        # insert initial Position
        payloads_Position = [
            Position(name='Software Engineer', details='Software Engineer'),
            Position(name='QA Engineer', details='QA Engineer'),
            Position(name='Project Manager', details='Project Manager'),
            Position(name='HR Manager', details='HR Manager'),
            Position(name='Accountant', details='Accountant'),
            Position(name='CEO', details='Chief Executive Officer'),
        ]
        session.add_all(payloads_Position)
        session.flush()

        # insert initial State
        payloads_State = [
            State(name='Active'),
            State(name='Inactive'),
        ]
        session.add_all(payloads_State)
        session.flush()

        session.commit()

        # insert initial data
        payloads_Employee = [
            Employee(
                username='Admin', password=hash_password('admin123'), name='Admin Doe', 
                position_id=payloads_Position[0].id, address='Jakarta', manager_id=None, 
                image=None, state_id=payloads_State[0].id),
            Employee(
                username='Max', password=hash_password('max123'), name='Max Doe', 
                position_id=payloads_Position[2].id, address='Jakarta', manager_id=1, 
                image=None, state_id=payloads_State[0].id),
            Employee(
                username='Jane', password=hash_password('jane123'), name='Jane Doe', 
                position_id=payloads_Position[3].id, address='Jakarta', manager_id=1, 
                image=None, state_id=payloads_State[0].id),
            Employee(
                username='John', password=hash_password('john123'), name='John Doe', 
                position_id=payloads_Position[4].id, address='Jakarta', manager_id=1, 
                image=None, state_id=payloads_State[0].id),
        ]
                     
        session.add_all(payloads_Employee)
        session.flush()

        # insert initial Department
        payloads_Department = [
            Department(name='IT Department', manager_id=payloads_Employee[1].id),
            Department(name='HR Department', manager_id=payloads_Employee[2].id),
            Department(name='Accounting Department', manager_id=payloads_Employee[3].id),
        ]
        session.add_all(payloads_Department)
        session.flush()

        session.commit()

        print('Database initialized successfully')
        print('Employees : ', payloads_Employee)
        print('Positions : ', payloads_Position)
        print('Departments : ', payloads_Department)
        print('States : ', payloads_State)
    except Exception as e:
        session.rollback()
        print(f"Error during database initialization: {str(e)}")
    finally:
        session.close()
