function extendBorrowingPeriod(docname) {
    var additionalDays = prompt("Enter the number of days to extend the borrowing period:");
    if (additionalDays) {
        frappe.call({
            method: "library_manegment.library_management.doctype.item_borrowing.item_borrowing.extend_borrowing_period", 
            args: {
                docname: docname,
                additional_days: parseInt(additionalDays)
            },
            callback: function(response) {
                frappe.msgprint(response.message);
                location.reload(); // إعادة تحميل الصفحة لتحديث البيانات
            }
        });
    }
}

// إضافة زر في صفحة Doctype
frappe.ui.form.on('Item Borrowing', {
    refresh: function (frm) {
        frm.add_custom_button(__('Extend Borrowing Period'), function() {
            extendBorrowingPeriod(frm.doc.name);
        });
    }
});