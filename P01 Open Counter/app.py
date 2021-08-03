from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///refresh.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



class Count(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    dt = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.dt}"



@app.route('/')
def hello_world():
    count = Count()
    db.session.add(count)
    db.session.commit()
    timesOpened = count.sno
    allCount = Count.query.all()

    return render_template("index.html", allCount = allCount, timesOpened = timesOpened)


if __name__ == "__main__":
    app.run(debug=True)