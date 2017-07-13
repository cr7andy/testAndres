from odoo import models,fields,api
from odoo.exceptions import UserError, ValidationError

class clsRubros(models.Model):
    _name='cri.rubros'
    
    codigo = fields.Char(string='Codigo', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Char(string='Descripcion')
    aniofiscal = fields.Integer('Anio Fiscal')
    
    @api.multi
    @api.constrains('codigo')
    def check_codido_rubro(self):
        raise UserError("self")
        #for rec in self:
         #   if rec:
          #      res = self.search([('codigo','=',rec.codigo),('id','!=',rec.id)])
           #     if res:
            #        raise UserError("Codigo repetido no se puede guardar")
        return True

        
    
class clsTipo(models.Model):
    _name='cri.tipo'
    
    codigo = fields.Char(string = "Codigo", required=True)
    nombre =  fields.Char(string = "Nombre", required=True)
    descripcion = fields.Char(string = "Descripcion")
    aniofiscal = fields.Integer("Anio Fiscal")
    rubro_id = fields.many2One("cri.rubros",string="CRI - Rubro")
    
class clsClase(models.Model):
    _name='cri.clase'
    
    codigo = fields.Char(string = "Codigo", required=True)
    nombre =  fields.Char(string = "Nombre", required=True)
    descripcion = fields.Char(string = "Descripcion")
    aniofiscal = fields.Integer("Anio Fiscal")
    tipo_id = fields.many2One("cri.tipo",string="CRI - Tipo")
    
class clsConcepto(models.Model):
    _name='cri.concepto'
    
    codigo = fields.Char(string = "Codigo", required=True)
    nombre =  fields.Char(string = "Nombre", required=True)
    descripcion = fields.Char(string = "Descripcion")
    aniofiscal = fields.Integer("Anio Fiscal")
    clase_id = fields.many2One("cri.clase",string="CRI - Clase")
    
class clsSubconcepto(models.Model):
    _name='cri.subconcepto'
    
    codigo = fields.Char(string = "Codigo", required=True)
    nombre =  fields.Char(string = "Nombre", required=True)
    descripcion = fields.Char(string = "Descripcion")
    aniofiscal = fields.Integer("Anio Fiscal")
    concepto_id = fields.many2One("cri.concepto",string="CRI - Concepto")
