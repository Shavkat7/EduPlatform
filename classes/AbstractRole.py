class AbstractRole:
    # Attributes common to all roles
    id: int
    full_name: str
    email: str
    password_hash: str
    created_at: str # ISO format

    # Methods common to all roles
    def __init__(self, id: int, full_name: str, email: str, password_hash: str, created_at: str):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
    
    def get_profile(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "created_at": self.created_at
        }
    
    def update_profile(self, full_name: str = None, email: str = None):
        if full_name:
            self.full_name = full_name
        if email:
            self.email = email
        return self.get_profile()
