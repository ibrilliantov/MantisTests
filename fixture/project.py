from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app


    # def create_new_project(self, project):
    #     wd = self.app.wd
    #     self.app.open_home_page
    #     self.app.open_project_home_page()
    #     wd.find_element_by_xpath("//input[@value='Create New Project']").click()
    #     self.fill_project_form(project)
    #     wd.find_element_by_name("submit").click()
    #     self.open_project_home_page()

    def add_new_project(self, project):
        wd = self.app.wd
        self.app.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.app.open_project_page()


    def fill_project_form(self, project):
        wd = self.app.wd
        self.fill_form_value("123Project_Name", project.name)
        self.fill_form_value("123description", project.description)

    def fill_form_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
