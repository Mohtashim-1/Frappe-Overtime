// Copyright (c) 2024, mohtashim and contributors
// For license information, please see license.txt

frappe.ui.form.on('Overtime', {
	refresh: function (frm) {
		// 		console.log("Fetching attendance data...");
		// 		let attendanceData = getAttendanceData({ date: frm.doc.posting_date });

		// 		// Check if child table population is required (optional)
		// 		if (shouldPopulateChildTable(frm)) {
		// 			console.log("Populating child table...");
		// 			for (let record of attendanceData) {
		// 				addChildRow(record);
		// 			}
		// 			frm.refresh_field('overtime_child');
		// 		}
		// 	}
		// });

		// // Assuming this function exists in your platform
		// function getAttendanceData(filters) {
		// 	console.log("Getting attendance data for:", filters.date);
		// 	let attendanceData = frappe.get_list("Attendance", {
		// 		filters: {
		// 			attendance_date: filters.date // Replace with the actual date field name
		// 		}

		// 	});
		// 	console.log('testing')
		// 	return attendanceData;
		// }

		// // Function to determine if child table needs population (optional)
		// function shouldPopulateChildTable(frm) {
		// 	// Implement logic to check if child table population is necessary
		// 	// This could involve checking a checkbox field or other criteria
		// 	// Return true if population is needed, false otherwise
		// 	return true; // Replace with your logic
		// }

		// // Replace with the actual function for adding rows to the child table
		// function addChildRow(data) {
		// 	console.log("Adding row for employee:", data.employee); // Assuming 'employee' field stores employee link
		// 	let newRow = frappe.ui.add_child('Overtime Child', frm.doc); // Replace with actual function
		// 	try {
		// 		newRow.attendance_record = data.name; // Assuming 'name' is the attendance record ID
		// 		newRow.employee_id = data.employee; // Assuming 'employee' field stores employee link
		// 		newRow.name1 = data.employee_name; // Assuming 'employee_name' stores employee name
		// 		// ... (set other field values based on data)
		// 	} catch (error) {
		// 		console.error("Error adding row:", error);
	}
}
)