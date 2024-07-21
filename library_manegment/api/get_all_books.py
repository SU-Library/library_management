import frappe

@frappe.whitelist(allow_guest=True)
def get_all_books():
    all_book =frappe.get_all(
        "Book",#اسم ال doctype
        fields= [ "name", "book_name", "cover_image"]
    )
    return all_book
