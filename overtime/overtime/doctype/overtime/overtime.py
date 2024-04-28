import frappe
from frappe.model.document import Document

class Overtime(Document):
    def overtime_hours(self):
        worked_hours = self.out_time - self.in_time
        total_seconds = total_seconds.total_seconds()
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        print(hours,":",minutes,":","seconds")
        print("Hours:", hours)
        print("Minutes:", minutes)
        print("Seconds:", seconds)    
        print(worked_hours)
        frappe.msgprint(worked_hours)

        
