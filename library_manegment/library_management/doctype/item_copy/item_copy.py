# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document.utils import Document ,barcode, data

class ItemCopy(Document):

   def generate_barcode_and_serial(ItemCopy, copy_code):
    # Generate barcode
    barcode_value = barcode.generate(barcode_type='Code39', value=copy_code, output='svg')

    # Generate serial number
    serial_number = data.get_next_auto_name(ItemCopy, prefix='SN-', increment=True)

    # Update the document with the generated barcode and serial number
    doc = frappe.get_doc(ItemCopy, copy_code)
    doc.barcode = barcode_value
    doc.serial_number = serial_number
    doc.save()