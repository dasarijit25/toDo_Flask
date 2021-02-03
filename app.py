from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done = False

    # def __repr__(self):
    #     return '<Content %s>' % self.content


db.create_all()


@app.route('/')
def tasks_list():
    fet = Task.query.all()
    return render_template('index.html', tasks=fet)
    

@app.route('/task', methods=['POST'])
def add_task():
    content = requeste.form['content']
    task = Task(contnt)
    db.session.add(task)
    db.session.commit()
    return redirect('/')
    
    
@app.route('/filter', methods = ['POST'])
def done_filter():
    if request.form['submit_button'] == 'done':
        fet = Task.query.filter_by(done=True).all()
        return render_template('index.html', tasks=fet)
        
    elif request.form['submit_button'] == 'remaining':
        fet = Task.query.filter_by(done=False).all()
        return render_template('index.html', tasks=fet)
        
    else:
        fet = Task.query.order_by(Task.content).all()
        return render_template('index.html', tasks=fet)


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    task = Task.query.get(task_id)
    
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)