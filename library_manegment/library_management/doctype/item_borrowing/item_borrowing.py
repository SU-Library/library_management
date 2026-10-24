# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date, now



class ItemBorrowing(Document):
    @frappe.whitelist()
    def extend_borrowing(self, days_n):
        new_date = add_to_date(self.expected_retrieval_date, days=days_n)
        return new_date

    @frappe.whitelist()
    def change_copy_status (self, new_status):
        frappe.db.set_value("Item Copy", self.item_copy , "status", new_status)

    @frappe.whitelist()
    def create_damage (self, description):
        new_damage = frappe.new_doc("Damage")
        new_damage.company = self.company
        new_damage.item_borrowing = self.name
        new_damage.description_of_the_damage = description
        new_damage.insert()

        copy_price = frappe.db.get_value("Item Copy", self.item_copy , "price")

        new_fine = frappe.new_doc("Fine")
        new_fine.company = self.company
        new_fine.item_borrowing = self.name
        new_fine.fine_type = "Damage"
        new_fine.damage = new_damage.name
        new_fine.fine_amount = copy_price
        new_fine.insert()

    def validate (self):
        pass

    def before_submit (self):

        # frappe.db.set_value("Item Borrowing", self.name, "status", "In Progress")
        day_no = frappe.get_value ( "Faculty Library Setting", self.company, "max_delay_period")
        self.date_of_borrowing = frappe.utils.nowdate()
        self.expected_retrieval_date = add_to_date(self.date_of_borrowing, days=day_no)

        library_setting = frappe.get_doc("Faculty Library Setting", self.company)
        available_books_no = library_setting.available_books_no

        maximum_no = 10

        for row in available_books_no:
            if row.role == self.role:
                maximum_no = row.max_books_no

        person_inprogress_borrowing = frappe.get_all ("Item Borrowing", filters = {
            "person": self.person, 
            "role": self.role,
            "status": "In Progress", 
            "docstatus": 1
        })

        if len(person_inprogress_borrowing) >= maximum_no:
            frappe.throw("تجاوز الحد المسموح")
        else:
            self.status = "In Progress"
            frappe.db.set_value("Item Copy", self.item_copy , "status", "Unavailable")