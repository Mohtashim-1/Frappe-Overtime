# import frappe
# from frappe.model.document import Document

# class Overtime(Document):
#     def get_attendance(self):
#         d = frappe.get_all("Attendance",filters={'attendance_date':self.posting_date},fields=['employee','in_time','out_time'])
#         self.overtime_hours = 10
#         frappe.msgprint(d)
#         self.posting_date = "2024-06-09"
        

#     def before_save(self):
#         # Calculate overtime hours
#         total_seconds = (self.out_time - self.in_time).total_seconds()
#         hours = total_seconds // 3600
#         minutes = (total_seconds % 3600) // 60
#         seconds = total_seconds % 60

#         # Create or update Overtime Child document
#         overtime_child = frappe.get_doc({
#             "doctype": "Overtime Child",
#             "parent": self.name,  # Link to the parent Overtime document
#             "check_in": self.in_time,
#             "check_out": self.out_time,
#             "overtime_hours": hours  # Save calculated overtime hours
#         })
#         overtime_child.save()


import frappe
from frappe.model.document import Document

class Overtime(Document):
    def get_attendance(self):
        try:
            # Debug message to check if the method is getting called
            frappe.msgprint("get_attendance method called")

            # Get attendance records for the posting date
            d = frappe.get_all("Attendance", filters={'attendance_date': self.posting_date},
                                fields=['employee', 'in_time', 'out_time'])

            # Debug message to check the attendance records retrieved
            frappe.msgprint(d)

            # Set a sample value to overtime_hours for testing
            self.overtime_hours = 10

            # Debug message to check if overtime_hours is set
            frappe.msgprint("overtime_hours set to 10")

            # Change the posting date for testing
            self.posting_date = "2024-06-09"

            # Debug message to indicate the method execution completed
            frappe.msgprint("Method execution completed")
        except Exception as e:
            # Handle any exceptions and print error message
            frappe.log_error("Error in get_attendance method: " + str(e))
            frappe.throw("An error occurred. Please check the error log for details.")
