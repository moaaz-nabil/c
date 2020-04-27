from odoo import models, fields,  _, api

class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment'
    appointment = fields.Many2one('hospital.appointment')
    patient = fields.Many2one('hospital.patient')
    patient_name = fields.Char()
    appointment_date = fields.Date()
    appointment_time = fields.Float()



    # Create Appointment Record Function
    def create_appointment(self):
        vals = {
            'patient' : self.patient.id,
            'date' : self.appointment_date,
            'time' : self.appointment_time
        }
        self.patient.message_post(body="Appointment Created Successfully", subject="Appointment Created")
        self.env['hospital.appointment'].create(vals)

    # Get Appointment Data
    def get_data(self):
        appointment_data = self.env['hospital.appointment'].search([('patient', '=', self.patient.id)])
        for rec in appointment_data:
            print ("Appointment", rec.patient_id)
            print ("Appointment", rec.patient_id)
            print ("Appointment", rec.patient_id)
            print ("Appointment", rec.patient_id)
            print ("Appointment", rec.patient_id)
            print ("Appointment", rec.patient_id)
            print ("Appointment", rec.patient_id)