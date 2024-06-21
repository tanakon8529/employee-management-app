
from utilities.database.position import read_position_table_by_condition, create_position_table, \
                            update_position_table_by_id, delete_position_table_by_id
from utilities.log_controler import LogControler
log_controler = LogControler()

def get_position_by_condition(data, db_session):
    return read_position_table_by_condition(data, db_session)

def post_position(data, db_session):
    result = create_position_table(data, db_session)
    db_session.commit()
    return result

def update_position(data, db_session):
    result = update_position_table_by_id(data, db_session)
    db_session.commit()
    return result

def delete_position_by_id(data, db_session):
    result = delete_position_table_by_id(data, db_session)
    db_session.commit()
    return result