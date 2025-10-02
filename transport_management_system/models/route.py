from odoo import models, fields


class Route(models.Model):
    _name = "route.regist"
    _description = "Route Info"
    _rec_name = "car_name"

    car_name = fields.Many2one("fleet.regist",
                                    string="Carro", required=True)
    origin = fields.Selection(
        [("luanda", "Luanda"),
         ("caxito", "Caxito"),
         ("bengo", "Bengo"),
         ("malanje", "Malanje")],
        string="Origen", required=True)
    destiny = fields.Selection(
        [("luanda", "Luanda"),
         ("caxito", "Caxito"),
         ("bengo", "Bengo"),
         ("malanje", "Malanje")],
    string="Destino", required=True)

    distance = fields.Float(string="Distancia", required=True)
    price = fields.Float(string="Custo Estimado", required=True)

