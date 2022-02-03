# -*- coding: utf-8 -*-
from odoo import models, api, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    cuota = fields.Float('Couta')
    cuota_cubierta = fields.Float('Couta cubierta')
    cuota_restante = fields.Float('Couta restante')

   