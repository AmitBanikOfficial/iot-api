try:
    from extensions import db,ma
    from sqlalchemy import Column, Integer, String
    print("Modules imported succssfully")
except Exception as e:
    print("Some modules are missing.")
    print(e)


# User database models
class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String,nullable = False, unique = True)
    password = Column(String,nullable = False)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)