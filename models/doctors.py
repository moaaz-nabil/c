from odoo import models, fields, api, _
    
class Doctor(models.Model):
    _name='hospital.doctors'

    name = fields.Char()
    phone = fields.Char()
    doctor_id = fields.Char(string="ID", required=True, copy=False, readonly=True,
                             index=True, default=lambda self: _('New'))
    doctor_pic = fields.Binary()                         

    category = fields.Selection([
        ('familyphysician','Family Physician'),
        ('internalmedicinephysician','Internal Medicine Physician'),
        ('pediatrician','Pediatrician'),
        ('surgeon','Surgeon'),
    ])
    patient_model_rel = fields.Many2many('hospital.patient')

    #Sequence Doctor Function    
    @api.model
    def create(self, vals):
        if vals.get('doctor_id', _('New')) == _('New'):
            vals['doctor_id'] = self.env['ir.sequence'].next_by_code('doctors.sequence') or _('New')
        result = super(Doctor, self).create(vals)
        return result