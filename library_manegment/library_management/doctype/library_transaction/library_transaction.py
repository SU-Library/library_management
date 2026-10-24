# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

"""Library Transaction: issue or return one physical copy of a reference item.

Flow (a submittable document):
  1. validate()        -> the member must hold a valid, submitted Library
                          Membership on the transaction date, and the chosen
                          copy must be in the right status for the action.
  2. before_submit()   -> the Item Copy status is flipped:
                          Issue  : Available   -> Unavailable
                          Return : Unavailable -> Available

Note: "Unavailable" is the Item Copy status used for a copy that is out on
loan (the Item Copy status options are Available / Unavailable / Damaged).
"""

import frappe
from frappe.model.document import Document
from frappe import _


class LibraryTransaction(Document):
    def validate(self):
        self.validate_membership()
        self.check_item_availability()

    def validate_membership(self):
        """Reject the transaction unless the member has a valid membership."""
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,  # submitted memberships only
                "from_date": ("<=", self.date),
                "to_date": (">=", self.date),
            },
        )

        if not valid_membership:
            frappe.throw(_("The member does not have a valid membership."))

    def check_item_availability(self):
        """Make sure the selected copy can be issued / returned."""
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
                'status': 'Unavailable'
            })
            if not on_loan_copy:
                frappe.throw(_('The selected copy {0} is not currently on loan').format(self.copy_number_identifier))

    def before_submit(self):
        """Update the Item Copy status according to the transaction type."""
        copy_filters = {
            'reference_item': self.reference_item,
            'select_doctype': self.select_doctype,
            'copy_identifier': self.copy_number_identifier
        }
        if self.type == 'Issue':
            frappe.db.set_value('Item Copy', copy_filters, 'status', 'Unavailable')
        elif self.type == 'Return':
            frappe.db.set_value('Item Copy', copy_filters, 'status', 'Available')
