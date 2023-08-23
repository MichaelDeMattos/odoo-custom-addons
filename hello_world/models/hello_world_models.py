# -*- coding: utf-8 -*-

from odoo import models, fields


class HelloWorldModel(models.Model):
    _name = 'hello.world.model'
    _description = 'Hello World Model'

    field_type_char = fields.Char(
        string='Field Type Char',
        size=256,
        help='Field Type Char')
    field_type_text = fields.Text(
        string='Field Type Text',
        help='Field Type Text')
    field_type_boolean = fields.Boolean(
        string='Field Type Boolean',
        help='Field Type Boolean')
    field_type_float = fields.Float(
        string='Field Type Float',
        digits=(16, 4),
        help='Field Type Float', )
    field_type_selection = fields.Selection(
        [('active', 'Active'), ('disabled', 'Disabled')],
        string='Field Type Selection')
    field_type_many2one = fields.Many2one(
        'sale.order',
        string='Field Type Many2One',
        help='Field Type Many2One Ref Sales Order')
    field_type_one2many_ids = fields.One2many(
        'hello.world.model.line',
        'field_type_many2one_id',
        string='Field Type One2Many Ref Hello World Model Line')


class HelloWorldModelLine(models.Model):
    _name = 'hello.world.model.line'
    _description = 'Hello World Model Line'

    field_type_char_line = fields.Char(
        string='Field Type Char',
        size=256,
        help='Field Type Char')
    field_type_many2one_id = fields.Many2one(
        'hello.world.model',
        string='Hello World Model')
