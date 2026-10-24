# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

"""Item Borrowing: one borrower (Employee or Student) borrows one Item Copy.

A submittable document with the status life cycle
    In Progress -> Returned | Overdue | Damaged

* before_submit()      : applies the faculty rules (loan period, maximum
                         number of simultaneous loans per role) and marks the
                         copy "Unavailable".
* extend_borrowing()   : returns the new expected return date (the form then
                         saves it).
* change_copy_status() : sets the Item Copy status (used when returning).
* create_damage()      : creates a Damage record and a Fine equal to the copy
                         price.
The overdue status and the "Delay" fine are handled by the daily job in
b_schedular.py.
"""

import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date, now



class ItemBorrowing(Document):
    @frappe.whitelist()
    def extend_borrowing(self, days_n):
        # Push the expected return date forward by days_n days.
        new_date = add_to_date(self.expected_retrieval_date, days=days_n)
        return new_date

    @frappe.whitelist()
    def change_copy_status (self, new_status):
        # e.g. "Available" when the copy is returned.
        frappe.db.set_value("Item Copy", self.item_copy , "status", new_status)

    @frappe.whitelist()
    def create_damage (self, description):
        # 1) record the damage, 2) fine the borrower the price of the copy.
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

        # Loan period (days) comes from the Faculty Library Setting of the company.
        day_no = frappe.get_value ( "Faculty Library Setting", self.company, "max_delay_period")
        self.date_of_borrowing = frappe.utils.nowdate()
        self.expected_retrieval_date = add_to_date(self.date_of_borrowing, days=day_no)

        library_setting = frappe.get_doc("Faculty Library Setting", self.company)
        available_books_no = library_setting.available_books_no

        maximum_no = 10  # default limit when no row exists for the borrower's role

        for row in available_books_no:
            if row.role == self.role:
                maximum_no = row.max_books_no

        # Count the borrower's submitted loans that are still in progress.
        person_inprogress_borrowing = frappe.get_all ("Item Borrowing", filters = {
            "person": self.person, 
            "role": self.role,
            "status": "In Progress", 
            "docstatus": 1
        })

        if len(person_inprogress_borrowing) >= maximum_no:
            frappe.throw("تجاوز الحد المسموح")  # maximum number of loans exceeded
        else:
            self.status = "In Progress"
            frappe.db.set_value("Item Copy", self.item_copy , "status", "Unavailable")