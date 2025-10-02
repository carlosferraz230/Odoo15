from odoo import models, fields


class Trip(models.Model):
    _name = "trip.regist"
    _description = "Trip Info"
    _rec_name = "destiny"

    car_name = fields.Many2one("fleet.regist",
                                    string="Veiculo", required=True)
    driver_id = fields.Many2one("driver.regist",
                                string="Motorista", required=True)
    destiny = fields.Many2one("route.regist",
                              string="Rota", required=True)
    arived_date = fields.Date(string="Data de Chegada", required=True)
    state = fields.Selection(
        [("draft", "Em Andamento"),
         ("confrimed", "Confirmado"),
         ("plan", "Planeada")],
        string="Estado", required=True)
