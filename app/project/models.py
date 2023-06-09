from flask_login import UserMixin
class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    def get_id(self):
        return int(self.id)
    
    def get_name(self):
        return self.username
    
    def is_authenticated(self):
        return True
