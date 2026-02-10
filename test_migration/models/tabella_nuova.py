from odoo import models, fields

class NuovaTabella(models.Model):
    _name = 'test.nuova_tabella' # Nome iniziale
    _description = 'Tabella Nuova'

    name = fields.Char(string="Nome")
