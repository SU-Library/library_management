// Copyright (c) 2024, us and contributors
// For license information, please see license.txt

frappe.ui.form.on("Item Borrowing", {
	refresh(frm) {
        if ( frm.doc.docstatus == 1 && frm.doc.status == "In Progress" ) {
            frm.add_custom_button(__(" Returned "), function(){
                frm.set_value("status", "Returned")
            
                frappe.call({
                    method: 'change_copy_status',
                    doc: frm.doc,
                    freeze: true,
                    freeze_message: __("Changing Book Status  ..."),
                    args:{
                        "new_status": "Available"
                    },
                    callback: function(r) {
                       frappe.msgprint("تم تعديل حالة الكتاب بنجاح");
                    }
                });
                frm.save("Update");
                
        });

        frm.add_custom_button(__(" Damage "), function(){
            frappe.prompt({
                label: __("Please Enter Description"),
                fieldname: "description",
                fieldtype: "Text"
            }, (values) => {
                frappe.call({
                    method: 'create_damage',
                    doc: frm.doc,
                    freeze: true,
                    args: {
                        "description": values['description']
                    },
                    freeze_message: __("Loading  ..."),
                    callback: function(r) {
                            console.log(r);
                            frm.set_value("status", "Damaged" )
                            frm.save("Update")
                            frappe.msgprint("تم ...")
                    }
                });
            });
           
        });

        frm.add_custom_button(__(" Extend Borrowing "), function(){
            
            frappe.prompt({
                label: __("Please Enter Days"),
                fieldname: "days",
                fieldtype: "Int"
            }, (values) => {
                console.log(values['days']);
                frappe.call({
                    method: 'extend_borrowing',
                    doc: frm.doc,
                    freeze: true,
                    args: {
                        "days_n": values['days']
                    },
                    freeze_message: __("Loading  ..."),
                    callback: function(r) {
                            console.log(r);
                            frm.set_value("expected_retrieval_date", r.message )
                            frm.save("Update")
                            frappe.msgprint("تم التمديد بنجاح")
                    }
                });
            },);
        });
        }
	},
},);
