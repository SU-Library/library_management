// Copyright (c) 2024, Us and contributors
// For license information, please see license.txt


/*frappe.ui.form.on('Graduation Project', {
    refresh: function(frm) {
        // Refresh the barcode field if the form is new
        if (frm.is_new()) {
            frm.refresh_field('barcode');
        }
    },
    after_save: function(frm) {
        frm.reload_doc();
    }
});*/



frappe.ui.form.on('Graduation Project', {
    onload: function(frm) {
        if (frm.doc.__islocal) {
            frm.events.autoname(frm);
        }
    },
    autoname: function(frm) {
        if (!frm.doc.barcode && frm.doc.project_title) {
            frm.set_value('barcode', frm.events.generate_barcode(frm));
        }
    },
    generate_barcode: function(frm) {
        if (!frm.doc.project_title) {
            frappe.msgprint('Please set the Project Title.');
            return '';
        }
        
        var name_parts = frm.doc.project_title.split(' ');
        var initials = '';
        for (var i = 0; i < name_parts.length; i++) {
            initials += name_parts[i][0].toUpperCase();
        }

        var timestamp = frappe.datetime.now_datetime();
        var timestamp_str = timestamp.replace(/[-: ]/g, '').slice(0, 14);  // Format YYYYMMDDHHMMSS
        
        var barcode = initials + timestamp_str;
        return barcode;
    }
});
