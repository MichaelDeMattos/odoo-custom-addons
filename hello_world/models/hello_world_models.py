# -*- coding: utf-8 -*-

from odoo import models, fields


class HelloWorldModel(models.Model):
    _name = "hello.world.model"
    _description = "Hello World Model"

    field_type_char = fields.Char(string="Field Type Char", size=256, help="Field Type Char")
    field_type_text = fields.Text(string="Field Type Text", help="Field Type Text")
