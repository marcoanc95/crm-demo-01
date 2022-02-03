# -*- coding: utf-8 -*-
from odoo import models, api, fields
from datetime import date, datetime

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    cuota = fields.Float('Couta')
    cuota_cubierta = fields.Float('Couta cubierta')
    cuota_restante = fields.Float('Couta restante')


    @api.onchange('expected_revenue', 'stage_id')
    def _on_change_cuota(self):
        for reg in self:
            fechaActual = datetime.today().date()
            linea_cuota = reg.sudo().env['crm.cuota'].search([('user_id', '=', reg.user_id.id), ('team_id', '=', reg.team_id.id), ('fecha_inicio', '<=', fechaActual), ('fecha_fin', '>=', fechaActual)])

            reg.update({
                    'cuota': linea_cuota.cuota,
                })

   