from odoo import models, fields

class Price(models.Model):
    _name = "trip_price.regist"
    _descrption = "Price Info"
    _rec_name = "price"

    gasoline = fields.Float(string="Combustível", required=True)
    peda = fields.Float(string="Pedágios", required=True)
    repair = fields.Float(string="Manutenção", required=True)
    price = fields.Float(string="Preço", required=True)