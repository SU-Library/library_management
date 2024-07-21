import frappe

@frappe.whitelist(allow_guest=True)
def get_book_details (book_name):
    book  = frappe.get_doc("Book", book_name)
    return {
        "book_name": book.name,
        "book_authors" : [{"name": a.author, "description" : a.description } for a in book.authors ],
        "image": "http://localhost:8001" + book.cover_image
    }