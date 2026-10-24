// Copyright (c) 2024, Us and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book", {
// 	refresh(frm) {

// 	},
// });

/*frappe.ui.form.on('Book', {
    refresh: function(frm) {
        if (!frm.doc.__islocal && !frm.doc.barcode) {
            frappe.call({
                method: 'your_app.your_module.doctype.book.book.generate_barcode',
                args: {
                    doc: frm.doc
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('barcode', r.message);
                        frm.save();
                    }
                }
            });
        }
    }
});
*/

frappe.ui.form.on('Book', {
    refresh : function(frm){
        
    },
    classification : function (frm){
        frm.set_value ("category", '');
    }
    // onload: function(frm) {
    //     if (frm.doc.__islocal) {
    //         frm.events.autoname(frm);
    //     }
    // },
    // autoname: function(frm) {
    //     if (!frm.doc.barcode && frm.doc.book_name) {
    //         frm.set_value('barcode', frm.events.generate_barcode(frm));
    //     }
    // },
    // generate_barcode: function(frm) {
    //     if (!frm.doc.book_name) {
    //         frappe.msgprint('Please set the Book Name.');
    //         return '';
    //     }
        
    //     var name_parts = frm.doc.book_name.split(' ');
    //     var initials = '';
    //     for (var i = 0; i < name_parts.length; i++) {
    //         initials += name_parts[i][0].toUpperCase();
    //     }

    //     var timestamp = frappe.datetime.now_datetime();
    //     var timestamp_str = timestamp.replace(/[-: ]/g, '').slice(0, 14);  // Format YYYYMMDDHHMMSS
        
    //     var barcode = initials + timestamp_str;
    //     return barcode;
    // }
});
