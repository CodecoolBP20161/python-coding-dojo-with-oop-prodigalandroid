
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


class Supplier(Contact):
    all_orders = dict()

    def order(self, string):
        all_orders[self.email] = string


class ContactList(Contact):

    def search(self, string):
        for contact in self.all_contacts:

