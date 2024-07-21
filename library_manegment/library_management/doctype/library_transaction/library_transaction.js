// Copyright (c) 2024, us and contributors
// For license information, please see license.txt



frappe.ui.form.on('Library Transaction', {
    select_doctype: function(frm) {
        if (frm.doc.select_doctype) {
            frm.set_value('reference_item', null);  // Clear the reference item field
            frm.set_value('copy_number_identifier', null);  // Clear the copy identifier field
            frm.set_query('reference_item', function() {
                return {
                    doctype: frm.doc.select_doctype,
                    filters: {}
                };
            });
            frm.set_df_property('copy_number_identifier', 'options', []);
            frm.refresh_field('copy_number_identifier');
        }
    },
    reference_item: function(frm) {
        frm.trigger('fetch_copy_identifiers');
    },
    type: function(frm) {
        frm.trigger('fetch_copy_identifiers');
    },
    fetch_copy_identifiers: function(frm) {
        if (frm.doc.reference_item && frm.doc.select_doctype && frm.doc.type) {
            let status_filter = frm.doc.type === 'Issue' ? 'Available' : 'On Loan';
            
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    doctype: 'Item Copy',
                    filters: {
                        reference_item: frm.doc.reference_item,
                        select_doctype: frm.doc.select_doctype,
                        status: status_filter
                    },
                    fields: ['name', 'copy_identifier', 'copy_barcode', 'status'],
                    limit_page_length: 1000
                },
                callback: function(r) {
                    if (r.message) {
                        let filtered_copies = r.message.filter(copy => copy.status === status_filter);
                        if (filtered_copies.length > 0) {
                            let copy_options = filtered_copies.map(copy => ({
                                label: `${copy.copy_identifier} - ${copy.copy_barcode}`,
                                value: copy.copy_identifier
                            }));
                            frm.set_df_property('copy_number_identifier', 'options', copy_options);
                            frm.refresh_field('copy_number_identifier');
                        } else {
                            frm.set_df_property('copy_number_identifier', 'options', []);
                            frm.refresh_field('copy_number_identifier');
                            frappe.msgprint({
                                title: __('No Copies Found'),
                                message: __('No copies with the status "{0}" found for this reference item.'.format(status_filter)),
                                indicator: 'red'
                            });
                        }
                    } else {
                        frm.set_df_property('copy_number_identifier', 'options', []);
                        frm.refresh_field('copy_number_identifier');
                        frappe.msgprint({
                            title: __('No Copies Found'),
                            message: __('No copies found for this reference item.'),
                            indicator: 'red'
                        });
                    }
                }
            });
        }
    }
});




