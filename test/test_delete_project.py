

from model.project import Project
import random



def test_delete_some_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.add_new_project(Project(name="te423st", description="desc24ription"))
    # old_list = db.get_project_list()
    old_list = app.soap.get_projects()
    project = random.choice(old_list)
    app.project.del_project(project.name)
    # new_list = db.get_project_list()
    new_list = app.soap.get_projects()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(old_list, key=Project.name_key) == sorted(new_list, key=Project.name_key)