# -*- coding: utf-8 -*-
# from odoo import http


# class AddonTest(http.Controller):
#     @http.route('/addon_test/addon_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addon_test/addon_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addon_test.listing', {
#             'root': '/addon_test/addon_test',
#             'objects': http.request.env['addon_test.addon_test'].search([]),
#         })

#     @http.route('/addon_test/addon_test/objects/<model("addon_test.addon_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addon_test.object', {
#             'object': obj
#         })
