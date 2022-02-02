# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class im_od_livestock_base(models.Model):
#     _name = 'im_od_livestock_base.im_od_livestock_base'
#     _description = 'im_od_livestock_base.im_od_livestock_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
