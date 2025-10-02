from odoo import models, fields

class Driver(models.Model):
    _name = "driver.regist"
    _description = "Driver Info"
    _rec_name = "driver_id"

    driver_id = fields.Char(string="Motorista", required=True)
    cnh = fields.Char(string="CNH", required=True)
    license_validity = fields.Date(
        string="Validade da Licença", required=True)
    availability = fields.Selection(
        [("yes", "SIM"), ("no", "Nao")],
        string="Disponibilidade", required=True)
    image = fields.Binary(string="Cover")