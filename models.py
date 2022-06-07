from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__="users"
    name=db.Column(db.String, primary_key=True)
    password=db.Column(db.String, nullable=False)
    timesta=db.Column(db.Integer, nullable=False)

class Book(db.Model):
    __tablename__="books"
    isbn=db.Column(db.String, primary_key=True)
    title=db.Column(db.String, nullable=False)
    author=db.Column(db.String, nullable=False)
    year=db.Column(db.Integer, nullable=False)
class Reviewer(db.Model):
    __tablename__="reviewer"
    isbn=db.Column(db.String, primary_key=True)
    name=db.Column(db.String, primary_key=True)
    rating=db.Column(db.Integer, nullable=False)
    review=db.Column(db.String, nullable=False)





# from flask import Flask, render_template, request
# # from flask_sqlalchemy import SQLAlchemy
# # from models import *
# # db=SQLAlchemy()


# app= Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# db.init_app(app)

# def main():
#     db.create_all()
# if __name__=="__main__":
#     with app.app_context():
#         main()