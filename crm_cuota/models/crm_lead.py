# -*- coding: utf-8 -*-
from odoo import models, api, fields
from datetime import date, datetime

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    cuota = fields.Float('Couta')
    cuota_cubierta = fields.Float('Couta cubierta')
    cuota_restante = fields.Float('Couta restante')

    def write(self, vals):
        res = super(CrmLead, self).write(vals)

        fechaActual = datetime.today().date()
        linea_cuota = self.sudo().env['crm.cuota'].search([('user_id', '=', self.user_id.id), ('team_id', '=', self.team_id.id), ('fecha_inicio', '<=', fechaActual), ('fecha_fin', '>=', fechaActual)])
        fechaInicio = linea_cuota[0].fecha_inicio
        fechaFin = linea_cuota[0].fecha_fin
        op_ganadas = self.sudo().env['crm.lead'].search([('user_id', '=', self.user_id.id), ('team_id', '=', self.team_id.id), ('won_status', '=', 'won'), ('date_closed', '>=', fechaInicio), ('date_closed', '<=', fechaFin)])
        avance = 0

        for op in op_ganadas:
            avance = avance + op.expected_revenue

        self.cuota = linea_cuota.cuota
        self.cuota_cubierta = avance
        self.cuota_restante = linea_cuota.cuota - avance

        return res






   