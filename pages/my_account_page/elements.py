from core.form_element import FormElement


class MyAccountPageElements:
    def __init__(self):
        self.my_account_menu = FormElement("LINK_TEXT", "My Account", "My Account Menu")
        self.username_textbox = FormElement("ID", "username", "Username Textbox")
        self.password_textbox = FormElement("ID", "password", "Password Textbox")
        self.login_button = FormElement("NAME", "login", "Login Button")
        self.myaccount_link = FormElement("LINK_TEXT", "Myaccount", "My Account Link")
        self.orders_link = FormElement("XPATH", '//*[@id="page-36"]/div/div[1]/nav/ul/li[2]/a', "Orders Link")
        self.orders_section = FormElement("CLASS_NAME", "order", "Orders Section")
