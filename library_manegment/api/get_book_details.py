"""Public API: details of one book (name, authors, cover image URL)."""

import frappe


@frappe.whitelist(allow_guest=True)  # public catalogue: no login required
def get_book_details(book_name):
    book = frappe.get_doc("Book", book_name)
    return {
        "book_name": book.name,
        "book_authors": [
            {"name": a.author, "description": a.description} for a in book.authors
        ],
        # Absolute URL built from the site's own address (no hard-coded host).
        "image": frappe.utils.get_url(book.cover_image) if book.cover_image else None,
    }
