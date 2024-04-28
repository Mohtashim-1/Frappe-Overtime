import frappe
from frappe.model.document import Document

class Overtime(Document):
    def validate(self):
        if not self.get('posting_date'):
            self.posting_date = "2024-06-09"
            frappe.msgprint('1')
        self.get_attendance()

    def get_attendance(self):
        d= frappe.db.get_all('Attendance', filters={
            'attendance_date':self.posting_date
        }, fields=[
            'employee', 'in_time', 'out_time'
        ])
        # d = frappe.get_all("Attendance", filters={'attendance_date': self.posting_date}, fields=['employee', 'in_time', 'out_time'])
        self.overtime_hours = 10
        frappe.msgprint('1')
        frappe.msgprint(d)
