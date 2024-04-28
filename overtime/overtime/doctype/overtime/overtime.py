import frappe
from frappe.model.document import Document

class Overtime(Document):
    def refresh(self):
        self.attendance_date =  self.get_attendance_date()

    def get_attendance_date(self):
        if not self.attendance_date:
            return[]
        attendance_records = frappe.get_all('Attendance',filters={'attendance_date':self.posting_date}, fields=['employee','check_in','check_out'])

    def populate_attendance_detail(self):
        if not self.attendance_date:
            return
        for record in self.attendance_records:
            new_row = self.append('Attendance Detail')
            new_row_employee = record.employee
            new_row_check_in = record.check_in
            new_row_check_out = record.check_out