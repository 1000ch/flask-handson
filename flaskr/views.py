import flask
from flaskr import app,db
from flaskr.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by('id desc').limit(10).all()
    return flask.render_template('show_entries.html', entries = entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
        title=flask.request.form['title'],
        title=flask.request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flask.flash('New entry was successfully posted')
    return flask.redirect(flask.url_for('show_entries'))