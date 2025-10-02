from odoo import models, fields


class FleetVehicle(models.Model):
    _name = "fleet.regist"
    _description = "Fleet Info"
    _rec_name = "car_name"

    car_name = fields.Char(string="Nome Do Carro", required=True)
    license_plate = fields.Char(string="Matricula Do Carro",
                                required=True)
    load_capacity = fields.Float(string="Capacidade De Carga",
                                 required=True)
    type = fields.Selection([
        ("heavy", "Pesado"),
        ("no_heavy", "Ligeiro")],
        string="Carga", required=True)
    driver_id = fields.Many2one("driver.regist",
                                string="Motorista")
