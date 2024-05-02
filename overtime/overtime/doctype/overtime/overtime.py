import frappe
from frappe.model.document import Document

class Overtime(Document):

    def before_save(self):
        self.salary()
        self.overtime_hour_calculation()

    
    def salary(self): 
        frappe.msgprint("testing...")
        self.per_hour_salary = float(self.ctc / 30 / 9)
        frappe.errprint(self.per_hour_salary)

    def overtime_hour_calculation(self):
        if(self.working_hours > 9 ):
            self.overtime_hour - self.working_hours
        else:
            self.overtime_hour = 0        