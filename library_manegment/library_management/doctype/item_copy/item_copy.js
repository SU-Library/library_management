// Copyright (c) 2024, us and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Item Copy", {
// 	refresh(frm) {

// 	},
// });


/*frappe.ui.form.on('Item Copy', {
    select_doctype: function(frm) {
        if (frm.doc.select_doctype) {
            frm.set_query('reference_item', function() {
                return {
                    'filters': {
                        'doctype': frm.doc.select_doctype
                    }
                };
            });
        }
    },
    reference_item: function(frm) {
        if (frm.doc.reference_item && frm.doc.select_doctype) {
            frappe.call({
                method: 'frappe.client.get_value',
                args: {
                    doctype: frm.doc.select_doctype,
                    filters: {
                        name: frm.doc.reference_item
                    },
                    fieldname: 'barcode'
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('original_barcode', r.message.barcode);

                        // Generate copy identifier
                        var name_parts = frm.doc.reference_item.split(' ');
                        var copy_id = '';
                        for (var i = 0; i < name_parts.length; i++) {
                            copy_id += name_parts[i][0].toUpperCase();
                        }

                        frappe.call({
                            method: 'frappe.client.get_list',
                            args: {
                                doctype: 'Item Copy',
                                filters: {
                                    reference_item: frm.doc.reference_item
                                },
                                fields: ['name'],
                                limit_page_length: 1000
                            },
                            callback: function(res) {
                                var count = res.message.length + 1;
                                var identifier = copy_id + ('0000' + count).slice(-4);
                                frm.set_value('copy_identifier', identifier);

                                // Set copy barcode
                                frm.set_value('copy_barcode', r.message.barcode + '-' + identifier);
                            }
                        });
                    }
                }
            });
        }
    }
});
*/


frappe.ui.form.on('Item Copy', {

    // select_doctype: function(frm) {
    //     // if (frm.doc.select_doctype) {
    //     //     frm.set_value('reference_item', null);  // Clear the reference item field
    //     //     frm.set_query('reference_item', function() {
    //     //         return {
    //     //             doctype: frm.doc.select_doctype,
    //     //             filters: {}
    //     //         };
    //     //     });
    //     }
    // },
    reference_item: function(frm) {
        if (frm.doc.reference_item != '') {
            if (frm.doc.select_doctype == "Book"){
                frappe.db.get_value ("Book", frm.doc.reference_item ,  "borrowable" ).then ((r) =>{
                    var i =  r['message']['borrowable'];
                    frm.set_value ("borrowable", i);
                })
            }
        }
        else {
            frm.set_value ("borrowable", 0 );
        }

        // if (frm.doc.reference_item && frm.doc.select_doctype) {
        //     frappe.call({
        //         method: 'frappe.client.get_value',
        //         args: {
        //             doctype: frm.doc.select_doctype,
        //             filters: {
        //                 name: frm.doc.reference_item
        //             },
        //             fieldname: [ 'cover_image']  // Fetch cover_image field
        //         },
        //         callback: function(r) {
        //             if (r.message) {
        //                 frm.set_value('original_barcode', r.message.barcode);
        //                 frm.set_value('item_cover', r.message.cover_image);  // Set item cover

        //                 // Generate copy identifier
        //                 var name_parts = frm.doc.reference_item.split(' ');
        //                 var copy_id = '';
        //                 for (var i = 0; i < name_parts.length; i++) {
        //                     copy_id += name_parts[i][0].toUpperCase();
        //                 }

        //                 frappe.call({
        //                     method: 'frappe.client.get_list',
        //                     args: {
        //                         doctype: 'Item Copy',
        //                         filters: {
        //                             reference_item: frm.doc.reference_item
        //                         },
        //                         fields: ['name'],
        //                         limit_page_length: 1000
        //                     },
        //                     callback: function(res) {
        //                         var count = res.message.length + 1;
        //                         var identifier = copy_id + ('0000' + count).slice(-4);
        //                         frm.set_value('copy_identifier', identifier);

        //                         // Set copy barcode
        //                         frm.set_value('copy_barcode', r.message.barcode + '-' + identifier);
        //                     }
        //                 });
        //             }
        //         }
        //     });
        // }
    }
});


