
from utilities.database.department import read_department_table_by_condition, create_department_table, \
                            update_department_table_by_id, delete_department_table_by_id
from utilities.log_controler import LogControler
log_controler = LogControler()

def get_department_by_condition(data, db_session):
    return read_department_table_by_condition(data, db_session)

def post_department(data, db_session):
    result = create_department_table(data, db_session)
    db_session.commit()
    return result

def update_department(data, db_session):
    result = update_department_table_by_id(data, db_session)
    db_session.commit()
    return result

def delete_department_by_id(data, db_session):
    result = delete_department_table_by_id(data, db_session)
    db_session.commit()
    return result