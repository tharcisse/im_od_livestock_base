# -*- coding: utf-8 -*-
# from odoo import http


# class ImOdLivestockBase(http.Controller):
#     @http.route('/im_od_livestock_base/im_od_livestock_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/im_od_livestock_base/im_od_livestock_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('im_od_livestock_base.listing', {
#             'root': '/im_od_livestock_base/im_od_livestock_base',
#             'objects': http.request.env['im_od_livestock_base.im_od_livestock_base'].search([]),
#         })

#     @http.route('/im_od_livestock_base/im_od_livestock_base/objects/<model("im_od_livestock_base.im_od_livestock_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('im_od_livestock_base.object', {
#             'object': obj
#         })
