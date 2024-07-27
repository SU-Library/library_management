frappe.ui.form.on('Unactivation Book', {
    refresh: function(frm) {
        if (frm.doc.book_copy) {
            frm.add_custom_button(__('Report Damage'), function() {
                frm.call({
                    method: "library_manegment.library_management.doctype.unactivation_book.unactivation_book.report_damage",
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        if (!r.exc) {
                            frm.refresh();
                        } else {
                            console.error('Error occurred:', r.exc);
                        }
                    }
                });
            });
        }
    }
});