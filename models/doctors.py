from odoo import models, fields

class DentalDoctor(models.Model):
    _name = 'dental.doctor'
    _description = 'Dental Doctor'

    doctor = fields.Many2one('res.partner', string="Doctor", required=True)
    service_id = fields.Many2one('dental.service', string="Service")
    image = fields.Binary(attachment=True)

    stage = fields.Selection([
        ('leave', 'Leave'),
        ('work', 'Work'),
    ], default='work', string='Status', required=True)

    def action_work(self):
        self.stage = 'work'
        

    def action_leave(self):
        self.stage = 'leave'
