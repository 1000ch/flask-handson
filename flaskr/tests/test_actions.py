import flaskr
from flaskr import app
from flaskr.models import Entry

def setup_module():
    flaskr.db.drop_all()
    flaskr.models.init()

def test_post_entry():
    client = app.test_client()
    response = client.post('/add', data={'title': 'test title 1', 'text': 'test text 1'}, follow_redirect=True)
    assert response.status_code == 200
    assert "test title 1" in response.data
    assert "test text 1 " in response.data
    with app.test_request_context():
        assert Entry.query.count() == 1
        entry = Entry.query.get(1)
        assert entry.title == 'test title 1'
        assert entry.text == 'test text 1'
