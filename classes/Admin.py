from classes.User import User


class Admin(User):

    # Attributes specific to Admin
    permissions: list  # List of permissions granted to the admin
    user_list: list  # List of users managed by the admin

    def __init__(self, id: int, full_name: str, email: str, password_hash: str, created_at: str, role: str):
        super().__init__(id, full_name, email, password_hash, created_at, role)
        self.permissions = []

    def add_user(self, user: User):
        new_user = User(user.id, user.full_name, user.email, user.password_hash, user.created_at, user.role)
        self.user_list.append(new_user)
        return new_user
    
    def remove_user(self, user_id):
        for user in self.user_list:
            if user.id == user_id:
                self.user_list.remove(user)
                return True
            
        return False
    
    def generate_report(self):
        return {
            "total_users": len(self.user_list),
            "permissions": self.permissions,
            "user_details": [user.get_profile() for user in self.user_list]
        }

