# -*- coding: utf-8 -*-
from odoo import models, api, fields
from datetime import date, datetime

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    cuota = fields.Float('Cuota', compute='_compute_cuota')
    cuota_cubierta = fields.Float('Cuota cubierta', compute='_compute_cuota')
    cuota_restante = fields.Float('Cuota restante', compute='_compute_cuota')

    @api.depends('expected_revenue', 'stage_id')
    def _compute_cuota(self):
        if self.expected_revenue:
            fechaActual = datetime.today().date()
            linea_cuota = self.sudo().env['crm.cuota'].search([('user_id', '=', self.user_id.id), ('team_id', '=', self.team_id.id), ('fecha_inicio', '<=', fechaActual), ('fecha_fin', '>=', fechaActual)])
            
            fechaInicio = linea_cuota[0].fecha_inicio
            fechaFin = linea_cuota[0].fecha_fin
            
            op_ganadas = self.sudo().env['crm.lead'].search([('user_id', '=', self.user_id.id), ('team_id', '=', self.team_id.id), ('won_status', '=', 'won'), ('date_closed', '>=', fechaInicio), ('date_closed', '<=', fechaFin)])
            
            avance = 0
            for op in op_ganadas:
                avance = avance + op.expected_revenue

            self.update({
                'cuota': linea_cuota.cuota,
                'cuota_cubierta': avance,
                'cuota_restante': linea_cuota.cuota - avance,
            })
