from odoo import models, fields, api, _

class patient(models.Model):
    _name='hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description='patient.record'
    _rec_name = 'name'

    patient_picture = fields.Binary(attachment=True)
    name = fields.Char(string="Name", track_visibility="always", required= True)
    age = fields.Integer(string="Age" , required= True)
    age_group = fields.Selection([
        ('adult','Adult'),
        ('children','Children'),
        ('baby','Baby')], readonly=True, compute='set_age_group' , required= True
    )
    phone = fields.Char()               
    gender = fields.Selection([
        ('male','Male'),
    ('famale','Famale'),
    ], required= True)
    patient_id = fields.Char(string="ID", required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    appointment_counter = fields.Char(compute='appointment_count')      
    active = fields.Boolean("Actice", default=True)                 

    @api.depends('age')
    def set_age_group(self):
        for rec in self:
            if rec.age :
                if rec.age < 5:
                    rec.age_group = 'baby'
                elif rec.age < 18 :
                    rec.age_group = 'children'
                else :
                    rec.age_group = 'adult'        


    @api.multi
    def open_patient_appointment(self):
        return {
            'name' : _('Appointment'),
            'domain' :  [('patient_id','=', self.patient_id)],
            'view_type' : 'form',
            'res_model' : 'hospital.appointment',
            'view_id' : False,
            'view_mode' : 'tree,form',
            'type' : 'ir.actions.act_window',
        }

    def appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.patient_id)])    
        self.appointment_counter = count

    
    #Sequence patient Function    
    @api.model
    def create(self, vals):
        if vals.get('patient_id', _('New')) == _('New'):
            vals['patient_id'] = self.env['ir.sequence'].next_by_code('patient.sequence') or _('New')
        result = super(patient, self).create(vals)
        return result


