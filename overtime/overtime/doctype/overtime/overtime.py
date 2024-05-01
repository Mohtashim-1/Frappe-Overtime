import frappe
from frappe.model.document import Document

class Overtime(Document):
    def before_save(self):
        frappe.msgprint('Message')
        
        self.ot_hours_calculation()


    def ot_hours_calculation(self):
        # Calculate overtime hours
        self.overtime_hours = self.working_hours - self.standard_hours
        # Save the document 
        self.save()

        # Optionally, you can also display a message to the user
        frappe.msgprint(f"Overtime hours calculated: {self.overtime_hours}")
