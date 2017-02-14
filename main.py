from peewee import *
from flask import *
from model import *

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def index():
    return redirect(url_for('list'))


@app.route('/and/list')
def list():
    sprinter = SuperSprinter.select().order_by(SuperSprinter.id)
    return render_template("list.html", sprinter=sprinter)


@app.route('/story/<id>', methods=['GET', 'POST'])
def story(id):
    if SuperSprinter.select().where(SuperSprinter.id == id).exists():
        user_story = SuperSprinter.get(SuperSprinter.id == id)
    else:
        user_story = None
    return render_template("form.html", user_story=user_story)


@app.route('/delete/<id>')
def delete(id):
    row = SuperSprinter.get(SuperSprinter.id == id)
    row.delete_instance()
    return redirect(url_for('list'))


@app.route('/add_story', methods=['GET', 'POST'])
def add_story():
    title = request.form['title']
    story = request.form['story']
    acceptance_criteria = request.form['criteria']
    business_value = request.form['business_value']
    estimation = request.form['estimation']
    status = request.form['status']
    new_story = SuperSprinter.create(title=title,
                                story=story,
                                acceptance_criteria=acceptance_criteria,
                                business_value=business_value,
                                estimation=estimation,
                                status=status)
    new_story.save()
    flash('New story successfully created!')
    return redirect(url_for('list'))


@app.route('/update_story', methods=['GET', 'POST'])
def update_story():
    id = request.form['id']
    title = request.form['title']
    story = request.form['story']
    acceptance_criteria = request.form['criteria']
    business_value = request.form['business_value']
    estimation = request.form['estimation']
    status = request.form['status']
    user_story = SuperSprinter.update(title=title,
                                 story=story,
                                 acceptance_criteria=acceptance_criteria,
                                 business_value=business_value,
                                 estimation=estimation,
                                 status=status).where(SuperSprinter.id == id)
    user_story.execute()
    return redirect(url_for('list'))


if __name__ == "__main__":
    app.run(debug=True)
