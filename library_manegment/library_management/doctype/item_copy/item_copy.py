# CopyItemright (c) 2024, us and contributors
# For license information, please see license.txt

# /your_custom_app/your_custom_app/doctype/copy_item/copy_item.py

import frappe
from frappe.model.document import Document
from frappe import _

class ItemCopy(Document):
    def validate(self):
        self.generate_barcodes()

    def generate_barcodes(self):
        # Generate Original Barcode if Reference Item is selected
        if self.reference_item:
            # Fetch the document of the reference item using doctype and item identifier
            reference_doc = frappe.get_doc(self.select_doctype, self.reference_item)
            self.original_barcode = reference_doc.barcode
            self.item_cover = reference_doc.cover_image

        # Generate Copy Barcode based on Original Barcode and Copy Identifier
        if self.original_barcode and self.copy_identifier:
            # Format the copy barcode using original barcode and copy identifier
            self.copy_barcode = f"{self.original_barcode}-{self.copy_identifier}"

    def on_update(self):
        # Ensure barcodes are generated whenever the document is updated
        self.generate_barcodes()

# Hook into the system (setup function can be used for additional setup if required)
def setup():
    pass