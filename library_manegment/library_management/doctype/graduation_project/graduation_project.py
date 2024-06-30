# Copyright (c) 2024, Us and contributors
# For license information, please see license.txt

# import frappe

'''import frappe
from frappe.model.document import Document
from datetime import datetime

class GraduationProject(Document):
    def before_insert(self):
        # Ensure the project title is set before generating the barcode
        if not self.project_title:
            frappe.throw("Project Title must be set before generating the barcode.")
        
        # Automatically generate a barcode
        self.barcode = self.generate_barcode()

    def generate_barcode(self):
        # Get first letter of each word in the project title
        name_parts = self.project_title.split()
        initials = ''.join([part[0].upper() for part in name_parts])

        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        # Combine initials and timestamp to create the barcode
        return f"{initials}{timestamp}"

'''
import frappe
from frappe.model.document import Document

class GraduationProject(Document):
    def autoname(self):
        # Automatically generate a barcode
        self.barcode = self.generate_barcode()

    def generate_barcode(self):
        if not self.project_title:
            frappe.throw("Project Title must be set before generating the barcode.")
        
        # Generate barcode based on project_title
        name_parts = self.project_title.split()
        initials = ''.join([part[0].upper() for part in name_parts])

        # Example: Combine initials with timestamp
        timestamp = frappe.utils.now_datetime()
        timestamp_str = timestamp.strftime('%Y%m%d%H%M%S')

        return f"{initials}{timestamp_str}"

@frappe.whitelist()
def generate_barcode(doc):
    project = frappe.get_doc(json.loads(doc))
    return project.generate_barcode()

