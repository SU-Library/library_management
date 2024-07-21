# Copyright (c) 2024, us and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe import _

class LibraryTransaction(Document):
    def validate(self):
        self.validate_membership()
        self.check_item_availability()

    def validate_membership(self):
        # Debug information
        frappe.log_error(message="Validating membership", title="Library Transaction Debug")

        # Check if a valid membership exists for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,  # Submitted status
                "from_date": ("<=", self.date),
                "to_date": (">=", self.date),
            },
        )

        # Debug output
        frappe.log_error(message=f"Membership found: {valid_membership}", title="Library Transaction Debug")

        if not valid_membership:
            frappe.throw(_("The member does not have a valid membership."))

    def check_item_availability(self):
        if self.type == 'Issue':
            available_copy = frappe.get_value('Item Copy', {
                'reference_item': self.reference_item,
                'select_doctype': self.select_doctype,
                'copy_identifier': self.copy_number_identifier,
                'status': 'Available'
            })
            if not available_copy:
                frappe.throw(_('The selected copy {0} is not available for issue').format(self.copy_number_identifier))
        elif self.type == 'Return':
            on_loan_copy = frappe.get_value('Item Copy', {
                'reference_item': self.reference_item,
                'select_doctype': self.select_doctype,
                'copy_identifier': self.copy_number_identifier,
                'status': 'On Loan'
            })
            if not on_loan_copy:
                frappe.throw(_('The selected copy {0} is not currently on loan').format(self.copy_number_identifier))

    def before_submit(self):
        # Update Item Copy status based on the transaction type
        if self.type == 'Issue':
            frappe.db.set_value('Item Copy', {
                'reference_item': self.reference_item,
                'select_doctype': self.select_doctype,
                'copy_identifier': self.copy_number_identifier
            }, 'status', 'On Loan')
        elif self.type == 'Return':
            frappe.db.set_value('Item Copy', {
                'reference_item': self.reference_item,
                'select_doctype': self.select_doctype,
                'copy_identifier': self.copy_number_identifier
            }, 'status', 'Available')

        # Additional logic for handling submissions (if any)
        # For example, log the transaction or update related documents
        frappe.log_error(message="Transaction is about to be submitted", title="Library Transaction Debug")

        # Example: Log a message for submission
        frappe.log_error(message=f"Submitting transaction: {self.name}", title="Library Transaction Debug")

