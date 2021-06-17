# -*- coding: utf-8 -*-
# from odoo import http


# class ThMinimalisticReportsAr(http.Controller):
#     @http.route('/th_minimalistic_reports_ar/th_minimalistic_reports_ar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/th_minimalistic_reports_ar/th_minimalistic_reports_ar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('th_minimalistic_reports_ar.listing', {
#             'root': '/th_minimalistic_reports_ar/th_minimalistic_reports_ar',
#             'objects': http.request.env['th_minimalistic_reports_ar.th_minimalistic_reports_ar'].search([]),
#         })

#     @http.route('/th_minimalistic_reports_ar/th_minimalistic_reports_ar/objects/<model("th_minimalistic_reports_ar.th_minimalistic_reports_ar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('th_minimalistic_reports_ar.object', {
#             'object': obj
#         })
