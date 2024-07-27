frappe.ui.form.on('fine', {
    item_borrowing: function (frm) {
        if (frm.doc.item_borrowing) {
            // تعيين قيمة الغرامة إلى 250
            frm.set_value('fine_amount', 250);
            
            // تعيين الحالة إلى "paid"
            frm.set_value('fine_status', 'paid');
        }
    }
});