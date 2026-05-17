from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date,datetime
from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URL")
db=SQLAlchemy(app)

class Status(Enum):
    Pending="Pending"
    Completed="Completed"
    Cancelled="Cancelled"

class ToDo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(500),nullable=False)
    date=db.Column(db.Date,nullable=False,default=date.today)
    time=db.Column(db.Time,nullable=False,default=datetime.now().time)
    status=db.Column(db.Enum(Status),nullable=False,default=Status.Pending)

    def __repr__(self)->str:
        return f"{self.id}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task', '').strip()
        if not task:
            return "Add a Task"
        
        newtask = ToDo(name=task)
        try:
            db.session.add(newtask)
            db.session.commit()
            return redirect('/')
        except:
            db.session.rollback()
            return redirect('/')
        return redirect('/')
    filter_status = request.args.get('filter', 'all')   # Get filter from URL
    query = ToDo.query
    if filter_status == 'pending':
        query = query.filter_by(status=Status.Pending)
    elif filter_status == 'completed':
        query = query.filter_by(status=Status.Completed)
    elif filter_status == 'cancelled':
        query = query.filter_by(status=Status.Cancelled)
    tasks = query.order_by(ToDo.date.desc(), ToDo.time.desc()).all()
    return render_template('index.html', tasks=tasks, current_filter=filter_status)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)