

def test_login123(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")