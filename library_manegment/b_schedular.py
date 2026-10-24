
import frappe
from datetime import datetime
@frappe.whitelist()
def check_overdue_borrowings():
    today = datetime.now().date()
    overdue_borrowings = frappe.get_all(
        "Item Borrowing",
        filters={
            "status": "In Progress",
            "expected_retrieval_date": ["<", today]
        },
        fields=["name", "company"]
    )

    for borrowing in overdue_borrowings:
        frappe.db.set_value("Item Borrowing", borrowing.name, "status", "Overdue")
        frappe.db.commit()  # Commit the changes to the database
    
        delay_fine_amount = frappe.db.get_value("Faculty Library Setting", borrowing.company , "delay_fine")
        new_fine =  frappe.new_doc("Fine")
        new_fine.company = borrowing.company
        new_fine.item_borrowing = borrowing.name
        new_fine.fine_type = "Delay"
        new_fine.fine_amount = delay_fine_amount
        new_fine.insert()
