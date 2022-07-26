from vedis import Vedis
import auth_data


def get_current_state(user_id):
    with Vedis(auth_data.db_file) as db:
        try:
            return db[user_id].decode() #
        except KeyError:
            return auth_data.States.S_START.value


def set_state(user_id, value):
    with Vedis(auth_data.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False