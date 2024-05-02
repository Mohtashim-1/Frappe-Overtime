// Copyright (c) 2024, mohtashim and contributors
// For license information, please see license.txt

frappe.ui.form.on('Overtime', {
	attendance_record: function (frm) {
		console.log(frm);
		var doc = frm.doc;
		var standard_hours = doc.standard_hours;
		var working_hours = doc.working_hours;
		// var per_hour_salary = 50000 / 30 / 9;
		// console.log(per_hour_salary)

		// Calculate overtime hours
		var ot_hours = working_hours - standard_hours;
		// console.log(ot_hours);

		// Set the value of the 'overtime_hours' field
		frm.set_value('ot_hours', ot_hours);
		// frm.set_value('per_hour_salary', per_hur_salary)
	}
});
