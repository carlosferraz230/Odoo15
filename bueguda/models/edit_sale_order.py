from odoo import models, fields
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    approval_date = fields.Date(string="Data de Aprovação")

    def action_confirm(self):
        # chama primeiro o método original
        res = super(SaleOrder, self).action_confirm()

        # atualizar campo com a data/hora atual
        for order in self:
            order.approval_date = fields.Datetime.now()
        return res


    def action_set_draft(self):
        for order in self:
            order.write({'state': 'draft'})
        return True
