import frappe

class UnactivationBook(frappe.model.document.Document):
    def validate(self):
        """تحديث حالة النسخ عند تسجيل تلف الكتاب"""
        if self.book_copy:
            # استرجاع النسخة من Item Copy بناءً على المعرف المحدد
            item_copy = frappe.get_doc('Item Copy', self.book_copy)
            if item_copy:
                # تحديث حالة النسخة إلى "تالف" عند تسجيل التلف
                item_copy.status = 'Damaged'  # أو الحالة المناسبة التي تريد تعيينها
                item_copy.save()
                frappe.db.commit()
                frappe.msgprint(f"Status updated to {item_copy.status} for Item Copy: {item_copy.name}")

    @frappe.whitelist()
    def report_damage(self):
        """دالة لتحديث حالة النسخ عند تسجيل التلف"""
        if self.book_copy:
            item_copy = frappe.get_doc('Item Copy', self.book_copy43)
            if item_copy:
                item_copy.status = 'Damaged'  # أو الحالة المناسبة التي تريد تعيينها
                item_copy.save()
                frappe.db.commit()
                frappe.msgprint(f"Status updated to {item_copy.status} for Item Copy: {item_copy.name}")