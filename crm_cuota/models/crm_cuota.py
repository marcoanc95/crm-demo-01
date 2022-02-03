# -*- coding: utf-8 -*-
from odoo import models, api, fields

class CrmCuota(models.Model):
    _name = 'crm.cuota'
    _description = 'Cuota'

    name = fields.Char('Nombre')
    user_id = fields.Many2one('res.users', string='Comercial')
    team_id = fields.Many2one('crm.team', string='Equipo de ventas')
    fecha_inicio = fields.Date('Fecha de inicio')
    fecha_fin = fields.Date('Fecha de fin')
    cuota = fields.Float('Couta')

   