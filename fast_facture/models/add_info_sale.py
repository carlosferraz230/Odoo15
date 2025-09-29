from odoo import models, fields


class AddInfo(models.Model):
    _inherit = "sale.order"

    type = fields.Selection(
        [("recieved_fature", "Fatura Recibo"),
         ("credit_note", "Nota De Credito"), ],
        string="Tipo", required=True)
    reference = fields.Char(string="Referencia")
    date = fields.Date(string="Data", readonly=True)
    to_pay = fields.Char(string="Por Pagar")
