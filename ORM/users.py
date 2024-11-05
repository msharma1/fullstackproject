from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://richatripathi@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<User {self.id}, {self.name}>'

@app.cli.command("init-db")
@with_appcontext
def init_db_command():
    """Create the database tables."""
    db.create_all()
    print("Initialized the database.")

    # Insert records
    users = [
        User(name='Bob'),
        User(name='Manish'),
        User(name='Richa'),
        User(name='Raghav'),
        User(name='Madhav')
    ]
    db.session.add_all(users)
    db.session.commit()
    print("Added users.")

@app.cli.command("query-users")
@with_appcontext
def query_users_command():
    """Query and print users."""
    # (2) Filter by name 'Bob'
    bob_users = User.query.filter_by(name='Bob').all()
    print("Users named Bob:", bob_users)

    # (3) LIKE query for names with 'b'
    b_users = User.query.filter(User.name.like('%b%')).all()
    print("Users with 'b' in their name:", b_users)

    # (4) First 5 records of the LIKE query
    first_5_b_users = User.query.filter(User.name.like('%b%')).limit(5).all()
    print("First 5 users with 'b' in their name:", first_5_b_users)

    # (5) Case-insensitive LIKE query
    case_insensitive_b_users = User.query.filter(User.name.ilike('%b%')).all()
    print("Case-insensitive users with 'b' in their name:", case_insensitive_b_users)

    # (6) Count users with name 'Bob'
    bob_count = User.query.filter_by(name='Bob').count()
    print("Number of users named Bob:", bob_count)

if __name__ == '__main__':
    app.run(debug=True)