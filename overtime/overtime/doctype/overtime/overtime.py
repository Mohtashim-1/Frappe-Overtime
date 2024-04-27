import frappe

def calculate_overtime(doc, method):
    # Fetch attendance records for the selected date
    attendance_records = frappe.get_all('Attendance', filters={'attendance_date': doc.posting_date}, fields=['employee', 'check_in', 'check_out'])

    # Iterate through each attendance record
    for record in attendance_records:
        hours_worked = calculate_hours_worked(record)
        if hours_worked > 5:
            overtime_hours = hours_worked - 5  # Subtract regular working hours
            add_overtime_record(doc, record.employee, overtime_hours)

def calculate_hours_worked(attendance_record):
    # Calculate total hours worked for an attendance record
    check_in = attendance_record.check_in
    check_out = attendance_record.check_out

    # Calculate time difference
    time_diff = check_out - check_in

    # Convert time difference to hours
    hours_worked = time_diff.total_seconds() / 3600

    return hours_worked

def add_overtime_record(doc, employee, overtime_hours):
    # Add overtime record to Overtime Child table
    child_table = doc.append('overtime_child', {})
    child_table.employee_id = employee
    child_table.overtime_hours = overtime_hours

    # Save the document
    doc.save()
