# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Student(Document):
	def validate (self): 
    		self.full_name = self.first_name + self.middle_name + self.last_name
