# Copyright (c) 2024, Us and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

'''class Book(Document):
    def autoname(self):
        # Automatically generate a barcode
        self.barcode = self.generate_barcode()

    def generate_barcode(self):
        last_barcode = frappe.db.sql("""
            SELECT barcode FROM `tabBook`
            ORDER BY creation DESC
            LIMIT 1
        """)
        
        if last_barcode:
            last_number = int(last_barcode[0][0])
            new_number = last_number + 1
        else:
            new_number = 1

        return str(new_number).zfill(8)  # Adjust the padding as per your requirement

@frappe.whitelist()
def generate_barcode(doc):
    book = frappe.get_doc(json.loads(doc))
    return book.generate_barcode()
'''

import frappe
from frappe.model.document import Document

class Book(Document):
    pass
    # def autoname(self):
    #     self.barcode = self.generate_barcode()

    # def generate_barcode(self):
    #     if not self.book_name:
    #         frappe.throw("Book Name must be set before generating the barcode.")
        
    #     # Generate barcode based on book_name
    #     name_parts = self.book_name.split()
    #     initials = ''.join([part[0].upper() for part in name_parts])

    #     # Example: Combine initials with timestamp
    #     timestamp = frappe.utils.now_datetime()
    #     timestamp_str = timestamp.strftime('%Y%m%d%H%M%S')

    #     return f"{initials}{timestamp_str}"

# @frappe.whitelist()
# def generate_barcode(doc):
#     book = frappe.get_doc(json.loads(doc))
#     return book.generate_barcode()
