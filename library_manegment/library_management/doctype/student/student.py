# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class Student(Document):
    def validate(self):
        # Join the non-empty name parts with single spaces.
        parts = [self.first_name, self.middle_name, self.last_name]
        self.full_name = " ".join(p for p in parts if p)
