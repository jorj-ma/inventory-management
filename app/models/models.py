from app.database.db import db

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def get_by_id(role_id):
        return Role.query.get(role_id)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    role = db.relationship("Role", backref="users")

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create(username, password, role_id):
        user = User(username=username, password=password, role_id=role_id)
        db.session.add(user)
        db.session.commit()
        return user


class Inventory(db.Model):
    __tablename__ = "inventory"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    @staticmethod
    def all():
        return Inventory.query.all()

    @staticmethod
    def add(item, quantity):
        inv = Inventory(item=item, quantity=quantity)
        db.session.add(inv)
        db.session.commit()
        return inv

    @staticmethod
    def update(item_id, quantity):
        inv = Inventory.query.get(item_id)
        if not inv:
            return None
        inv.quantity = quantity
        db.session.commit()
        return inv

    @staticmethod
    def delete(item_id):
        inv = Inventory.query.get(item_id)
        if not inv:
            return False
        db.session.delete(inv)
        db.session.commit()
        return True
