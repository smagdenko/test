from selenium import webdriver

class GroupSession:

    def __init__(self, app):
        self.app=app

    def create(self, group):

        driver = self.app.driver
        driver.find_element_by_xpath(".//*[@id='nav']/ul/li[3]/a").click()
        driver.find_element_by_xpath(".//*[@id='content']/form/input[1]").click()
        # New group
        self.fill_group_name(group)

    def fill_group_name(self, group):
        driver = self.app.driver
        self.change_field_text("field_name", group.name)
        self.change_field_text("field_header", group.header)
        self.change_field_text("field_footer", group.footer)
        driver.find_element_by_name("submit").click()

    def change_field_text(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)


    def delete(self):
        driver = self.app.driver
        driver.find_element_by_xpath(".//*[@id='nav']/ul/li[3]/a").click()
        groups=driver.find_elements_by_xpath("//*[@id='content']//span")
        for _ in range(len(groups)):
            driver.find_element_by_xpath("//*[@id='content']//span[1]").click()
            driver.find_element_by_xpath("//input[2][@name='delete']").click()
            driver.find_element_by_xpath(".//*[@id='content']//a[contains(.,'group page')]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver

        # driver.find_element_by_xpath(".//*[@id='maintable']//tr[2]//input").click()
        driver.find_element_by_xpath("//*[@id='nav']//a[contains(.,'groups')]").click()
        # open modification form
        driver.find_element_by_xpath("//input[3][@name='edit']").click()
        # fill group form
        self.fill_group_name(new_group_data)
        # submit modification
        driver.find_element_by_xpath(".//*[@id='content']/form/input[3]").click()
        driver.find_element_by_xpath(".//*[@id='content']//a[contains(.,'group page')]").click()



