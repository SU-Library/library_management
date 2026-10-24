# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

"""Unactivation Book: take a physical copy out of circulation.

A submittable document. Submitting it marks the linked Item Copy as
"Damaged"; cancelling it puts the copy back to "Available".
"""

import frappe
from frappe.model.document import Document


class UnactivationBook(Document):
    def on_submit(self):
        self._set_copy_status("Damaged")

    def on_cancel(self):
        self._set_copy_status("Available")

    def _set_copy_status(self, status):
        if self.book_copy:
            frappe.db.set_value("Item Copy", self.book_copy, "status", status)
            frappe.msgprint(f"Item Copy {self.book_copy} is now {status}")
