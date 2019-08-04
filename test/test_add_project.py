



#
# def test_add_project(app):
#     # contact = json_contacts
#     # old_contacts = db.get_contact_list()
#     app.project.add_new_project(project)
#     # new_contacts = db.get_contact_list()
#     # assert len(old_contacts) + 1 == len(new_contacts)
#     # old_contacts.append(contact)
#     # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#     # if check_ui:
#     #     assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)




from model.project import Project


def test_add_project(app, json_project):
    project = json_project
    # old_list = db.get_project_list()
    app.project.add_new_project(project)
    # new_list = db.get_project_list()
    # assert len(old_list) + 1 == len(new_list)
    # old_list.append(project)
    # assert sorted(old_list, key=Project.name_key) == sorted(new_list, key=Project.name_key)