// Copyright (c) 2024, mohtashim and contributors
// For license information, please see license.txt

frappe.ui.form.on('Overtime', {
	refresh: function (frm) {
		// console.log(frm)
		// var doc = frm

	}
}
)

// frappe.ui.form.on('Overtime Child', {
// 	check_out: function (frm, cdt, cdn) {
// 		calculateOvertime(frm, cdt, cdn);
// 	},
// 	check_in: function (frm, cdt, cdn) {
// 		calculateOvertime(frm, cdt, cdn);
// 	}
// });

// function calculateOvertime(frm, cdt, cdn) {
// 	var doc = frappe.get_doc(cdt, cdn);
// 	var check_in = doc.check_in;
// 	var check_out = doc.check_out;

// 	// Calculate the difference in milliseconds
// 	var timeDiff = check_out - check_in;

// 	// Convert milliseconds to hours
// 	var hours = timeDiff / (1000 * 3600);

// 	// Set the value of overtime_hours in the current Overtime Child record
// 	frappe.model.set_value(cdt, cdn, 'overtime_hours', hours);
// }
