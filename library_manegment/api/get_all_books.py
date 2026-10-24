"""Public API: list of all books (name, title, cover image)."""

import frappe


@frappe.whitelist(allow_guest=True)  # public catalogue: no login required
def get_all_books():
    return frappe.get_all(
        "Book",
        fields=["name", "book_name", "cover_image"],
    )
