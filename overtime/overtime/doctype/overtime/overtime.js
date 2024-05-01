// Copyright (c) 2024, mohtashim and contributors
// For license information, please see license.txt

frappe.ui.form.on('Overtime', {
	attendance_record: function (frm) {
		console.log(frm);
		var data = frm.doc;
		var standard_hours = data.standard_hours;
		var working_hours = data.working_hours;

		// Calculate overtime hours
		var ot_hours = working_hours - standard_hours;
		console.log(ot_hours);

		// Set the value of the 'overtime_hours' field
		frm.set_value('ot_hours', ot_hours);
	}
});
