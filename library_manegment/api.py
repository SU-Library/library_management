import frappe

@frappe.whitelist()
def get_books ():
    books = frappe.get_all ("Item", filters = {
        "name": [ "like",  "8" ]
    })
    return books


