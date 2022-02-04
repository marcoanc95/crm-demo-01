# -*- coding: utf-8 -*-
from odoo import models, api, fields
from datetime import date, datetime

class GetCrmCuotaReport(models.TransientModel):
    _name = 'get.crm.cuota.report'
    _description = 'Obtener Reporte de cuota'

    team_ids = fields.Many2many('crm.team', string="Equipos de venta")


    def create_report(self):
        self.env['crm.cuota.report'].search([]).unlink()

        for team in self.team_ids:
            for user in team.member_ids:
                fechaActual = datetime.today().date()
                linea_cuota = self.sudo().env['crm.cuota'].search([('user_id', '=', user.id), ('team_id', '=', team.id), ('fecha_inicio', '<=', fechaActual), ('fecha_fin', '>=', fechaActual)])

                fechaInicio = linea_cuota[0].fecha_inicio
                fechaFin = linea_cuota[0].fecha_fin

                op_ganadas = self.sudo().env['crm.lead'].search([('user_id', '=', user.id), ('team_id', '=', team.id), ('won_status', '=', 'won'), ('date_closed', '>=', fechaInicio), ('date_closed', '<=', fechaFin)])

                avance = 0
                for op in op_ganadas:
                    avance = avance + op.expected_revenue

                 
                values = {
                    'name': linea_cuota[0].name,
                    'user_id': user.id,
                    'team_id': team.id,
                    'fecha_inicio': fechaInicio,
                    'fecha_fin': fechaFin,
                    'cuota': linea_cuota[0].cuota,
                    'cuota_cubierta': avance,
                    'cuota_restante': linea_cuota[0].cuota - avance,
                }
                linea = self.env['crm.cuota.report'].create(values)

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'crm.cuota.report',
            'views': [(False, 'tree')],
            'target': 'current',
        }
        