# Copyright (c) 2024, us and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import timedelta

class ItemBorrowing(Document):
    def extend_borrowing_period(self, additional_days):
        if self.status != "Borrowed":
            return "Cannot extend period for this status."
        
        # احسب تاريخ الاسترجاع الجديد
        new_expected_date = self.expected_retrieval_date + timedelta(days=additional_days)
        self.expected_retrieval_date = new_expected_date
        
        # قم بحفظ التحديث
        self.save()
        frappe.db.commit()
        
        return "Borrowing period extended successfully."

# الوظيفة المتاحة على الواجهة الأمامية
@frappe.whitelist()
def extend_borrowing_period(docname, additional_days):
    doc = frappe.get_doc("Item Borrowing", docname)
    return doc.extend_borrowing_period(int(additional_days))