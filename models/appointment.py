from odoo import models, fields, api, _

class appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'patient.appintment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name='patient'

    patient = fields.Many2one('hospital.patient', required= True)
    patient_pic = fields.Binary(related='patient.patient_picture', readonly=True)
    patient_phone = fields.Char(related='patient.phone', readonly=True)
    patient_id = fields.Char(related='patient.patient_id', readonly=True)
    date = fields.Date(required= True)
    time = fields.Float()
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('done','Done'),
    ], readonly=True, default='draft')

    def confirm_button(self):
        for rec in self:
            rec.state = 'confirm'

    def done_button(self):
        for rec in self:
            rec.state = 'done'        

    pharmcy_note = fields.Text()
    doctor_note  = fields.Text()
    # create_appointment_rel  = fields.Many2many('create.appointment')   