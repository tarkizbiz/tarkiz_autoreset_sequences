# -*- coding: utf-8 -*-
from odoo import http

# class AsaAutoresetSquence(http.Controller):
#     @http.route('/asa_autoreset_squence/asa_autoreset_squence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asa_autoreset_squence/asa_autoreset_squence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asa_autoreset_squence.listing', {
#             'root': '/asa_autoreset_squence/asa_autoreset_squence',
#             'objects': http.request.env['asa_autoreset_squence.asa_autoreset_squence'].search([]),
#         })

#     @http.route('/asa_autoreset_squence/asa_autoreset_squence/objects/<model("asa_autoreset_squence.asa_autoreset_squence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asa_autoreset_squence.object', {
#             'object': obj
#         })