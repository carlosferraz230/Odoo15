from odoo import models, fields, api
from datetime import datetime


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_code = fields.Char(
        string="Código Interno do Cliente",
        readonly=True,
        copy=False,
        index=True
    )

    @api.model
    def create(self, vals):
        if vals.get('customer_code', 'New') == 'New':
            vals['customer_code'] = self.env['ir.sequence'].next_by_code('bueguda.seq') or 'New'
        return super(ResPartner, self).create(vals)
