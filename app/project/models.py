from flask_login import UserMixin, login_user, current_user, logout_user, login_required

class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    def get_id(self):
        return str(self.id)
