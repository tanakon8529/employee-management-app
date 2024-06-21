
from utilities.database.state import read_state_table_by_condition, create_state_table, \
                            update_state_table_by_id, delete_state_table_by_id
from utilities.log_controler import LogControler
log_controler = LogControler()

def get_state_by_condition(data, db_session):
    return read_state_table_by_condition(data, db_session)

def post_state(data, db_session):
    result = create_state_table(data, db_session)
    db_session.commit()
    return result

def update_state(data, db_session):
    result = update_state_table_by_id(data, db_session)
    db_session.commit()
    return result

def delete_state_by_id(data, db_session):
    result = delete_state_table_by_id(data, db_session)
    db_session.commit()
    return result