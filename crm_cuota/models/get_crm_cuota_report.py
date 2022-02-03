# -*- coding: utf-8 -*-
from odoo import models, api, fields

class GetCrmCuotaReport(models.TransientModel):
    _name = 'get.crm.cuota.report'
    _description = 'Obtener Reporte de cuota'

    team_ids = fields.Many2many('crm.team', string="Equipos de venta")


    def create_report(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'crm.cuota.report',
            'views': [(False, 'tree')],
            'target': 'current',
        }
        