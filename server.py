from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'
#app.config['SQLALCHEMY_DATABASE_URI']=''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    image=db.Column(db.String(20),nullable=False)
    titre=db.Column(db.String(20),nullable=False)
    prix=db.Column(db.Float,nullable=False)
    specs=db.Column(db.String(60),nullable=False)
    description=db.Column(db.Text,nullable=False)
    
    
    


class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(20),nullable=False)
    mail=db.Column(db.String(20),nullable=False)
    mdate=db.Column(db.DateTime,default=datetime.datetime.utcnow)
    rate=db.Column(db.Integer,nullable=False)
    message=db.Column(db.Text,nullable=False)

messages=[]



@app.route("/")
def home():
    products=Product.query.all()
    x=datetime.datetime.now().date()
    return render_template("home.html",today=x, prods=products, titre="Home")

@app.route("/about")
def about():
    return  render_template("about.html",titre="About")


@app.route("/contact",methods=['GET','POST'])
def contact():
    valid=False
    if request.method=="POST":
        nom=request.form.get("nom")
        mail=request.form.get("mail")
        message=request.form.get("message")
        mdate=request.form.get("mdate")
        rate=request.form.get("rate")
        msg=Message(nom=nom, mail=mail,message=message,mdate=mdate,rate=rate)
        db.session.add(msg)
        db.session.commit()
        valid=True
    messages=Message.query.all()
    return  render_template("contact.html",valid=valid,messages=messages[::-1])

@app.route("/product/<id>")
def product(id):
    id=int(id)-1
    products=Product.query.all()
    return render_template('product.html',prod=products[id])


if __name__=="__main__":
    app.run(debug=True)