# -*- coding: utf-8 -*-
from odoo import models, api, fields

class CrmCuotaReport(models.Model):
    _name = 'crm.cuota.report'
    _description = 'Cuota Report'

    name = fields.Char('Nombre')
    user_id = fields.Many2one('res.users', string='Comercial')
    team_id = fields.Many2one('crm.team', string='Equipo de ventas')
    fecha_inicio = fields.Date('Fecha de inicio')
    fecha_fin = fields.Date('Fecha de fin')
    cuota = fields.Float('Cuota')
    cuota_cubierta = fields.Float('Cuota cubierta')
    cuota_restante = fields.Float('Cuota restante')

   