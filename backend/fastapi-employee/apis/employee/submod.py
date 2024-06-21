
from utilities.database.employee import read_employee_table_by_condition, read_signin_by_username_password, create_employee_table, \
                            update_employee_table_by_id, delete_employee_table_by_id
from utilities.log_controler import LogControler
log_controler = LogControler()

def get_employee_by_condition(data, db_session):
    return read_employee_table_by_condition(data, db_session)

def signin_employee_by_username_password(data, db_session):
    return read_signin_by_username_password(data, db_session)

def post_employee(data, db_session):
    result = create_employee_table(data, db_session)
    db_session.commit()
    return result

def update_employee(data, db_session):
    result = update_employee_table_by_id(data, db_session)
    db_session.commit()
    return result

def delete_employee_by_id(data, db_session):
    result = delete_employee_table_by_id(data, db_session)
    db_session.commit()
    return result