from odoo import models, fields


class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True)
    reference = fields.Char(string='Reference')
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    availability = fields.Boolean(string='Available', default=True)
    user_id = fields.Many2one('res.users', string='Responsible')
    category_id = fields.Many2one(
        'real.estate.category',
        string='Category',
    )

    def action_reserve(self):
        self.ensure_one()
        self.availability = False
