from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title=db.Column(db.String(100), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default= datetime.utcnow)


    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}" 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
    todo= Todo(title=title, desc=desc)
    db.session.add(todo)
    db.sesion.commit()  
    allTodo = Todo.query.all()
    print(allTodo)                                             
    return  render_template("index.html", allTodo=allTodo)
@app.route('/update')
def update():
    allTodo = Todo.query.all()
    print(allTodo)
    return 
@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno)
    db.session.delete(todo)
    db.session.commit()
    return


if __name__ =="__main__":
    app.run(debug=True, port=8000)
