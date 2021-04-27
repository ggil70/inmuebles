
# -*- coding= utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http=//tiny.be>).
#
#    This program is free software= you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http=//www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
# from osv import fields,osv --- <8.0.X
from odoo import api, fields, models
from odoo.exceptions import ValidationError
#from Datetime import Date, Datetime,timedelta
##############from odoo.addons.jasper_reports import jasper_report
#from odoo import pooler
#from Datetime import  Datetime
from time import time
formatter_string = "%d-%m-%y" 
#from tools.translate import_
#from odoo import tools
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
#Importamos la libreria logger
import logging
#Definimos la Variable Global
_logger = logging.getLogger(__name__)



class bienes_inmuebles(models.Model):
    """Registro de Bienes Inmuebles (edificios)"""
    _name = 'bienes_inmuebles'
    _rec_name = 'bienes_numbien'
    _order = 'bienes_numbien'  
   # _rec_name =  'bienes_nombre'
    #_rec_name = 'bienes_numbien_ant'
    #_rec_name = 'bienes_serial
    #_rec_name = 'grupo_bien_id'
    #_rec_name = 'clasificador_bien_id'
    #_rec_name = 'modelo_bien_id'
    #_rec_name = 'detalle_modelo_id'
    #_rec_name = 'color_id'
    #_rec_name = 'material_id'
    #_rec_name = 'oficinas_id'
    #_rec_name = 'marcas_id'
    #_rec_name = 'modelo_fab_id'
    #_rec_name = 'medidas'
    #_rec_name = 'resp_uso_id'
    #_rec_name = 'resp_pat_id'
    #_rec_name = 'costo'
    #_rec_name = 'estatus_uso_id'
    #_rec_name = 'estatus_bien_id'
    #_rec_name = 'detalle_adquisi_id'
    #_rec_name = 'catalogo_sudebi_id'
    #_rec_name = 'catalogo_sudebi_sub_id'
    #_rec_name = 'catalogo_sudebi_esp_id'
    #_rec_name = 'estado_id'
    #_rec_name = 'municipios_id'
    #_rec_name = 'parroquias_id'
    #_rec_name = 'poliza_id'
    #_rec_name = 'clase_sudebi_id'
    



    detalle_adquisi_id = fields.Many2one('detalle_adquisi', 'Detalle de Aquisicion del Bien', size=3,required=True,help ='Registra el detalle de la Adquisición del Bien')
    detalle_adquisi_codigo   = fields.Char(string='Código del Detalle',size=12,
                              help='Registra el Codigo del Detalle de la Adquisicion del Bien')

    forma_adquisicion_codigo = fields.Char(string='Codigo de la Forma de Adquisicion',size=3, help='Registra el Codigo de la Forma de Adquisicion')


    
    tipo_bien_id      = fields.Many2one('tipo_bien',  'Tipo de Bien', size=10, help='Registra el Código del Tipo de Bien')
    tipo_bien_codigo = fields.Char(string='Codigo del Tipo de Bien',size=10,required=True, help='Registra el Codigo del Tipo de Bien')


    bienes_numbien = fields.Char('Numero del Bien',size=20,
                     help='Registra el Numero de Bien Nacional')
    bienes_nombre  = fields.Text('Descripcion del Bien', size=300, help='Registra la Descripcion del Bien')
    
    estatus_uso_id = fields.Many2one('estatus_uso', 'Estatus de Uso', size=3, required=True,help='Registra el Estatus de Uso del Bien ')
    estatus_uso_codigo = fields.Char(string='Codigo del Estatus de Uso',size=3, help='Registra el Codigo de uso del bien')

    estado_bien_id = fields.Many2one('estado_bien', 'Estatus del Bien', size=3,required=True,help='Registra el Estatus del Bien ')
    estado_bien_codigo = fields.Char(string='Codigo del Estado del Bien',size=3,required=True, help='Registra el Codigo del Estado del Bien')

    costo = fields.Float('Costo de Bien', help='Registra el Costo del Bien',digits=(20, 7))

    #color_sudebi_id = fields.Many2one('color_sudebi','Color segun (SUDEBIP)', help='Registra el Color segun SUDEBIP')
    #color_sudebi_codigo = fields.Char(string='Codigo del Color segun Sudebip',size=3, help='Registra el Codigo de Color segun (SUDEBIP)')



    catalogo_sudebi_id = fields.Many2one('catalogo_sudebi', 'Categoría  General(SUDEBIP)', domain="[('catalogo_sudebi_codigo','=','31000-0000')]", required=True,help='Registra el Catalogo General de la SUDEBIP')
    catalogo_sudebi_codigo   = fields.Char(string='Codigo de la Categoria',size=10,required=True, help='Codigo de la Categoria General de la (SUDEBIP)')

    catalogo_sudebi_sub_id = fields.Many2one('catalogo_sudebi_sub','Categoría  Sub-General(SUDEBIP)', domain="[('catalogo_sudebi_id','=',catalogo_sudebi_id)]", help='Registra la Categoria Sub- General de la SUDEBIP')
    catalogo_sudebi_sub_codigo  = fields.Char(string='Codigo de la SubCategoria',size=10,required=True, help='Codigo de la Categoria Sub-General de la (SUDEBIP)')


    catalogo_sudebi_esp_id = fields.Many2one('catalogo_sudebi_esp','Categoría  Específica (SUDEBIP)', domain="[('catalogo_sudebi_sub_id','=',catalogo_sudebi_sub_id)]",help='Registra la Categoria Específica de la SUDEBIP')
    catalogo_sudebi_esp_codigo   = fields.Char(string='Codigo de la Categoria Específica',size=10, help='Codigo de la Categoria Especifica de la (SUDEBIP)')

    ano_construc =fields.Integer('Año de Construcción',size=4,help='Registra el año de Construcción del Bien')
    edad_construc =fields.Integer('Edad de Construcción',size=4,help='Registra la  Edad de Construcción del Bien')

    
    agua_potable = fields.Selection([('S','Si'),('N','No')],'Posee Agua Potable',  size=1, help='Registra si el Bien posee Agua Potable')
    electricidad = fields.Selection([('S','Si'),('N','No')],'Posee Electricidad',  size=1, help='Registra si el Bien posee Electricidad')

    agua_servida = fields.Selection([('S','Si'),('N','No')],'Posee Agua Servidad',  size=1, help='Registra si el Bien posee Aguas Servidas')

    telefono = fields.Selection([('S','Si'),('N','No')],'Posee Teléfono',  size=1, help='Registra si el Bien posee Teléfono')

    internet = fields.Selection([('S','Si'),('N','No')],'Posee Internet',  size=1, help='Registra si el Bien posee Internet')

    poso_aguas_profundas = fields.Selection([('S','Si'),('N','No')],'Posee  Poso de Aguas Profundas',  size=1, help='Registra si el Bien Posee  Poso de Aguas Profundas')

    poso_séptico = fields.Selection([('S','Si'),('N','No')],'Posee  Poso Séptico',  size=1, help='Registra si el Bien Posee  Poso Séptico')

    planta_electrica = fields.Selection([('S','Si'),('N','No')],'Posee Planta Eléctrica',  size=1, help='Registra si el Bien Posee  Planta Eléctrica')
    capacidad_planta_electrica = fields.Selection([('S','Si'),('N','No')],'Posee Planta Eléctrica',  size=1, help='Registra si el Bien Posee  Planta Eléctrica')

    estado_ocupacion_inmueble_id = fields.Many2one('estado_ocupacion_inmueble', help='Registra el Estado de Oocupación del Inmueble')   
    estado_ocupacion_inmueble_nombre = fields.Char(string='Nombre del Estado de ocupacion del Inmueble',size=40, help='Registra la Descripcion del Estado de ocupacion del Inmueble')

    #unidad_medida_area_sin_construccion_id = fields.Many2one('unidad_medida_construccion', 'Unidad de Medida del Área de Sin Construcción (SUDEBIP)', size=3, required=True,help='Registra la Unidad de Medida del Área sin Construcción')
    #unidad_medida_area_sin_construccion_codigo  = fields.Char(string='Codigo de la Unidad de Medida',size=6,required=True, help='Registra el Codigo del Área de Sin Construcción')


    uso_inmueble_id = fields.Many2one('uso_inmueble', 'Uso del Inmueble', size=3, required=True,help='Registra el Uso del Inmueble')
    uso_inmueble_codigo = fields.Char(string='Codigo del Uso del Inmueble',size=3,required=True, help='Registra el Codigo de Uso del Inmueble')

    area_construccion = fields.Float('Area de la Construcción ocupada por el edificio',size=50, help='Registra el Area de la construcción ocupada por el Edificio')

    unidad_medida_construccion_id = fields.Many2one('unidad_medida_construccion', 'Unidad de Medida del Área de Construcción (SUDEBIP)', size=3, required=True,help='Registra la Unidad de Medida del Área de Construcción')
    unidad_medida_construccion_codigo  = fields.Char(string='Codigo de la Unidad de Medida',size=6,required=True, help='Registra el Codigo del Proveedor del Bien')

    area_terreno    = fields.Float('Area Total del Terreno M2', help='Registra el área total del terreno en metros cuadrados')
   
    unidad_medida_terreno_id = fields.Many2one('unidad_medida_terreno', 'Unidad de Medida del Área del Terreno (SUDEBIP)', size=3, required=True,help='Registra la Unidad de Medida del Área de Construcción')
    unidad_medida_terreno_codigo  = fields.Char(string='Codigo de la Unidad de Medida',size=6,required=True, help='Registra el Codigo del Proveedor del Bien')

    uso_comforme = fields.Char(string='Uso Conforme',size=100, help='Registra el Uso Conforme')
    otro_uso = fields.Char(string='Otro Uso ',size=100, help='Registra el Otro Uso del Bien')

    urbanizacion = fields.Text('Urbanizacion', size=100)
    calle = fields.Text('Calle / Avenida', size=100)
    casa_edificio = fields.Text('Casa / Edificio', size=100)
    parroquias_id = fields.Many2one('mppp_reg_pro_parroquias', 'Parroquia donde se encuentra el Bien', domain="[('municipios_id','=',municipios_id)]",size=3, help='Registra la Parroquia donde se encuentra el Bien')   
    parroquias_codigo = fields.Char(string='Codigo de la Parroquia',size=3, help='Registra el Codigo de la Parroquia')

    ciudad_id = fields.Many2one('mppp_reg_pro_ciudad', 'Ciudad donde se encuentra el Bien', size=3, domain="[('municipios_id','=',municipios_id)]",help='Registra la Ciudad donde se encuentra el Bien')   
    ciudad_codigo = fields.Char(string='Codigo de la ciudad',size=3, help='Registra el Codigo de la Ciudad')

    municipios_id = fields.Many2one('mppp_reg_pro_municipios', 'Municipio donde se encuentra el Bien', size=3, domain="[('estado_id','=',estados_id)]",help='Registra el Municipio donde se encuentra el Bien')   
    municipios_codigo = fields.Char(string='Codigo del Municipio',size=3, help='Registra el Codigo del Municipio')

    estados_id = fields.Many2one('mppp_reg_pro_estados', 'Estado donde se encuentra el Bien', size=3, help='Registra el Estado donde se encuentra el Bien')   
    estados_codigo = fields.Char(string='Codigo del Estado',size=3, help='Registra el Codigo del Estado')

    paises_id = fields.Many2one('paises', 'País donde se encuentra el Bien', size=3, help='Registra el País donde se encuentra el Bien')   
    paises_codigo = fields.Char(string='Codigo del País',size=3, help='Registra el Codigo del País')

    direccion       = fields.Text('Dirección del Inmueble',size=255, help='Registra cual es la Dirección del Inmueble')

    otra_ciudad       = fields.Text('Otra Ciudad',size=50, help='Registra Otra Ciudad donde esta del Inmueble')
    otro_pais       = fields.Text('Otra País',size=50, help='Registra Otra País donde esta del Inmueble')

    es_sede = fields.Selection([('S','Si'),('N','No')],'¿Es sede?',  size=1, help='Registra si el Bien es Sede del órgano o ente')
    localizacion = fields.Selection([('N','Nacional'),('I','Internaional')],'Localización',  size=1, help='Registra la Localización del  Bien ')
    linderos_norte    = fields.Char('Linderos Norte del Inmueble',size=150, help='Registra los Linderos Norte del Inmueble')  
    linderos_sur    = fields.Char('Linderos Sur del Inmueble',size=150, help='Registra los Linderos Sur del Inmueble')  
    linderos_este   = fields.Char('Linderos Este del Inmueble',size=150, help='Registra los Linderos Este del Inmueble')  
    linderos_oeste    = fields.Char('Linderos Oeste del Inmueble',size=150, help='Registra los Linderos Oeste del Inmueble')  
    coordenadas   = fields.Char('Coordenadas del Inmueble',size=150, help='Registra los Linderos Oeste del Inmueble')  


    bienes_piso   = fields.Integer('Pisos',size=2, help='Registra el numero de Pisos que tiene el Edificio')
    grupo_bien_id = fields.Many2one('grupo_bien', 'Grupo del Bien', size=3, domain="[('grupo_bien_codigo','=',16)]", required=True,help='Registra el Grupo al Cual Pertenece el Bien')   
    grupo_bien_codigo =  fields.Char(string='Codigo del Grupo',size=3,  required=True,help='Registra el Codigo del Grupo (Interna)')


    clasificador_bien_id = fields.Many2one('clasificador_bien', 'Clasificador del Bien',required=True, domain="[('grupo_bien_id','=', grupo_bien_id)]", size=3, help='Registra el Codigo de Clase del Bien')
    clasificador_codigo = fields.Char(string='Codigo de la Clase',
                          size=3,
                          required=True,
                        
                          help='Registra el Codigo de la Clase del Bien (Interna)')

    modelo_bien_id = fields.Many2one('modelo_bien', 'Modelo del Bien', size=3,domain="[('clasificador_id','=',clasificador_bien_id)]", help='Registra el Modelo del Bien')   
    modelo_codigo = fields.Char(string='Codigo del Modelo',size=3,
                    required=True,
                    help='Registra el Codigo del Modelo (Interno)')


    detalle_modelo_id = fields.Many2one('detalle_modelo_bien', 'Tipo de Inmueble Según su Uso', size=3, domain="[('modelo_id','=',modelo_bien_id)]", help='Registra el Tipo de Inmueble Según su Uso')
    detalle_modelo_codigo = fields.Char(string='Codigo del Detalle',
                            size=3,
                            
                            help='Registra el Codigo del Detalle del Modelo de Bienes (Interno)') 

    funcionabilidad = fields.Char('Funcionabilidad del Inmueble',size=50, help='Registra cual esl la Funcionabiliad del Inmueble')
  
    area_total_construccion = fields.Float('Area Total de la Construcción (Total de los Pisos) M2',size=50, help='Registra el  Area Total de la Construcción (Total de los Pisos) M2')  
    area_anexos = fields.Float('Area de las Anexidades (Jardines, Patios, Etc)',size=50, help='Registra el  Area de las Anexidades (Jardines, Patios, Etc')  
    
    estudio_legal = fields.Char('Estudio Legal del Inmueble',size=150, help='Registra el Estudio Legal del Inmueble') 
    clase_funcional_terr_ids = fields.Many2many('clase_funcional_terr', 'terreno_clasfun_rel','bienes_inmuebles_id','clase_funcional_terr_id',string='Clasficicación Funcional del Terreno', size=3,help='Registra la Clasificacion Funcional del Terreno')
    clase_funcional_terr_codigo = fields.Char(string='Codigo del Tipo de Anexo',size=3,help='Registra el Codigo de la Clasificación Funcional del Terreno')


    hectareas           = fields.Float(string='Hectareas de Terreno', help='Registra el Hectareas de Terreno')
    metros_cuadrados    = fields.Float(string='Metros Cuadrados de Terreno', help='Registra los Metros Cuadrados de Terreno')
    vias_interiores     = fields.Char('Vías Interiores Longitud y Especificaciones',size=200, help='Vías Interiores Longitud y Especificaciones del terreno')
    otras_bienhechurias = fields.Char('Resúmen del detalle de las Bienhechurías',size=200, help='Resúmen del detalle de las Bienhechurías del terreno')

    bienes_oficinas_id = fields.Many2one('oficinas', 'Oficina', size=3, required=True, domain="[('sedes_id','=',bienes_sedes_id)]",help='Registra la Oficina donde esta Ubicado el Bien')
    bienes_oficinas_codigo       = fields.Char(string='Nomenclatura de la Oficina',size=20,required=True, help='Registra la Nomenclatura de la Oficina')

    bienes_sedes_id  = fields.Many2one('sedes',string='Sedes del Ministerio', required=True, domain="[('regiones_id','=',bienes_regiones_id)]",help='Registra el Codigo de Vinculacion con las Sedes del Ministerio')
    bienes_sedes_codigo       = fields.Char(string='Código de la Sede',size=7,required=True, help='Registra el Código de la Sede')

    bienes_regiones_id  = fields.Many2one('regiones',string= 'Regiones de Ubicación de la Sede',size=3, required=True ,help='Regiones de Ubicación de la Sede')    
    bienes_regiones_codigo       = fields.Char(string='Codigo de la Región',size=3,required=True, help='Registra el Codigo de la Región')

    resp_uso_id = fields.Many2one('personas', 'Responsable de Uso', domain="[('personas_oficinas_id','=', bienes_oficinas_id)]", size=3, required=True,help='Registra el Responsable del Uso del Bien')
    cedu_resp_uso = fields.Integer(string='Cédula del Responsable de Uso',size=10,required=True, help='Registra la Cedula de la persona')



    poliza_id = fields.Many2one('poliza','Poliza de Seguro', size=3)
    poliza_codigo        = fields.Char(string='Codigo de la Poliza',size=3, help='Registra el Codigo de la Poliza')

    fech_inventario = fields.Date('Fecha de Registro en el Inventario', size=8,help='Registra la Fecha de Registro en el Inventario de la Oficina')   
    observacion =   fields.Text('Observaciones al Bien', help='Registra las Observaciones al Bien')
    active = fields.Boolean ('Activo', default=True, help='Si esta Activo el motro lo icluira en la vista') 
    sw_desin = fields.Boolean ('Desincorporado', help='Registra si el bien fue Desincorporado')    
  
    bienes_ministerio_id =  fields.Many2one('bienes_ministerio',string='Información del Ministerio para la Remisión', help='Registra la Información del Ministerio para la Remisión del Inventario')
    bienes_ministerio_codigo = fields.Char(string='Codigo de la Información del Ministerio para la Remisión',
                      size=3,
                      help='Registra el Codigo de la Información del Ministerio para la Remisión')


    #estructura_ids = fields.Many2many('estructura_inmueble', 'edificio_estructura_rel','bienes_inmuebles_id','estructura_id',string='Estructura', size=3, help='Registra el Tipo de Estructura del Inmueble')

    #tipo_piso_ids = fields.Many2many('tipo_piso', 'edificio_tipo_piso_rel','bienes_inmuebles_id','tipo_piso_id','Tipo de Piso', size=3,help='Registra el Tipo de Piso del Inmueble')
    #tipo_paredes_ids = fields.Many2many('tipo_paredes', 'edificio_tipo_paredes_rel','bienes_inmuebles_id',string='Tipos de Paredes', size=3, help='Registra el Tipo de Paredes del Inmueble')
    #tipo_techo_ids = fields.Many2many('tipo_techo', 'edificio_tipo_techo_rel','bienes_inmuebles_id',string='Tipos de Techo', size=3, help='Registra el Tipo de Techo del Inmueble')
    #tipo_puertas_ids = fields.Many2many('tipo_puertas', 'edificio_tipo_puertas_rel','bienes_inmuebles_id',string='Tipos de Puertas', size=3, help='Registra el Tipo de Puertas del Inmueble')
    #tipo_servicios_ids = fields.Many2many('tipo_servicios', 'edificio_tipo_servicios_rel','bienes_inmuebles_id',string='Tipos de Servicios', size=3, help='Registra el Tipo de Servicios del Inmueble')
    #tipo_anexos_ids = fields.Many2many('tipo_anexos', 'edificio_tipo_anexos_rel','bienes_inmuebles_id',string='Tipos de Anexos', size=3, help='Registra el Tipo de Anexos del Inmueble')
    #remodelaciones_ids = fields.One2many('remodelaciones','bienes_inmuebles_id', string='Remodelaciones')
    @api.onchange('bienes_numbien')
    def onchange_bienes_numbien(self):
        if self.bienes_numbien:
            num_bien = self.bienes_numbien
            domain = [('numbien','=',num_bien)]            
            recordset= self.env['control_bienes'].search(domain)
            if recordset:
                self.bienes_numbien = ""
                for registro in recordset:
                    mensaje = "El número de bien registrado [" + registro['numbien']  + "] ya se encuentra registrado como un Bien [" + registro['tipo_bienes'] + "]"  
                    warning = {
                        'title': "Advertencia!",
                        'message': mensaje,
                }    
                return {'warning': warning }    
          
          
          
    @api.model
    def create(self, value):
        diccionario = {'numbien': value['bienes_numbien'], 
                            'tipo_bienes': 'INMUEBLES',
        }
        registro = self.env['control_bienes'].create(diccionario)  
        rec = super(bienes, self).create(value)
        return rec        




    @api.onchange('bienes_regiones_id')
    def onchange_bienes_regiones(self):
        codigor= ''
        codigor = self.bienes_regiones_id.regiones_codigo
        self.bienes_regiones_codigo =  codigor


    @api.onchange('bienes_sedes_id')
    def onchange_bienes_sedes(self):
        codigos= ''
        codigos = self.bienes_sedes_id.sedes_codigo
        self.bienes_sedes_codigo =  codigos
    
    @api.onchange('bienes_oficinas_id')
    def onchange_bienes_oficinas(self):
        codigoo= ''
        codigoo = self.bienes_oficinas_id.oficinas_codigo
        self.bienes_oficinas_codigo =  codigoo

    @api.onchange('resp_uso_id')
    def onchange_resp_uso(self):
        codigore= ''
        codigore = self.resp_uso_id.personas_cedula
        self.cedu_resp_uso =  codigore

    @api.onchange('tipo_bien_id')
    def onchange_tipo_bien(self):
        codigo= ''
        codigo = self.tipo_bien_id.tipo_bien_codigo
        self.tipo_bien_codigo =  codigo




    @api.onchange('grupo_bien_id')
    def onchange_grupo(self):
        codigo= ''
        codigo = self.grupo_bien_id.grupo_bien_codigo
        self.grupo_bien_codigo =  codigo
        self.clasificador_bien_id = ''
       
      
    @api.onchange('clasificador_bien_id')
    def onchange_clasif(self):
            
    
        codigoc= ''
        codigoc = self.clasificador_bien_id.clasificador_codigo
        self.clasificador_codigo =  codigoc
        self.modelo_bien_id =  ''

       
    @api.onchange('modelo_bien_id')
    def onchange_modelo(self):
        codigom= ''
        codigom = self.modelo_bien_id.modelo_codigo
        self.modelo_codigo =  codigom
        self.detalle_modelo_id =  ''

    
    @api.onchange('grupo_bien_id','clasificador_bien_id','modelo_bien_id','detalle_modelo_id')
    def onchange_categorias(self):
        catego =''
        detamod = ''
       
        if self.clasificador_bien_id.clasificador_nombre:
            catego += str(self.clasificador_bien_id.clasificador_nombre)
        if self.modelo_bien_id.modelo_nombre:
              catego += ' '+ str(self.modelo_bien_id.modelo_nombre)
        if self.detalle_modelo_id.detalle_modelo_nombre:
            if self.detalle_modelo_id.detalle_modelo_nombre != False:
                self.detalle_modelo_codigo = self.detalle_modelo_id.detalle_modelo_codigo

                catego += ' '+str(self.detalle_modelo_id.detalle_modelo_nombre)
        self.bienes_nombre = catego
   
    @api.onchange('estatus_uso_id')
    def onchange_estatus_uso(self):
        codigo= ''
        codigo = self.estatus_uso_id.estatus_uso_codigo
        self.estatus_uso_codigo =  codigo

    @api.onchange('estado_bien_id')
    def onchange_estado_bien(self):
        codigo= ''
        codigo = self.estado_bien_id.estado_bien_codigo
        self.estado_bien_codigo =  codigo   

    @api.onchange('detalle_adquisi_id')
    def onchange_detalle_adquisi(self):
        codigo= ''
        codigoad =''
        codigo = self.detalle_adquisi_id.detalle_adquisi_codigo
        codigoad = self.detalle_adquisi_id.codigo_ad
        self.detalle_adquisi_codigo =  codigo
        self.forma_adquisicion_codigo = codigoad

    @api.onchange('catalogo_sudebi_id')
    def onchange_catalogo_sudebi(self):
        codigo= ''
        codigo = self.catalogo_sudebi_id.catalogo_sudebi_codigo
        self.catalogo_sudebi_codigo =  codigo

    @api.onchange('catalogo_sudebi_sub_id')
    def onchange_catalogo_sudebi_sub(self):
        codigo= ''
        codigo = self.catalogo_sudebi_sub_id.catalogo_sudebi_sub_codigo
        self.catalogo_sudebi_sub_codigo =  codigo

    @api.onchange('catalogo_sudebi_esp_id')
    def onchange_catalogo_sudebi_esp(self):
        codigo= ''
        codigo = self.catalogo_sudebi_esp_id.catalogo_sudebi_esp_codigo
        self.catalogo_sudebi_esp_codigo =  codigo


    # @api.onchange('color_sudebi_id')
    # def onchange_color_sudebi(self):
    #     codigo= ''
    #     codigo = self.color_sudebi_id.color_sudebi_codigo
    #     self.color_sudebi_codigo =  codigo


    @api.onchange('poliza_id')
    def onchange_poliza(self):
        codigo= ''
        codigo = self.poliza_id.poliza_codigo
        self.poliza_codigo =  codigo


    @api.onchange('unidad_medida_construccion')
    def onchange_medida_construccion(self):
        codigomc= ''
        codigomc = self.unidad_medida_construccion_id.unidad_medida_construccion_codigo
        self.unidad_medida_construccion_codigo =  codigomc


    @api.onchange('unidad_medida_terreno')
    def onchange_medida_terreno(self):
        codigomt= ''
        codigomt = self.unidad_medida_terreno_id.unidad_medida_terreno_codigo
        self.unidad_medida_terreno_codigo =  codigomt


    @api.onchange('estado_ocupacion_inmueble')
    def onchange_estado_ocupacion_inmueble(self):
        codigooi= ''
        codigooi = self.estado_ocupacion_inmueble_id.estado_ocupacion_inmueble_codigo
        self.estado_ocupacion_inmueble_codigo =  codigooi


    # @api.model
    # def create(self, vals):
    #     vals['bienes_numbien'] = self.env['ir.sequence'].next_by_code('bienes_inmuebles.bienes_numbien')
        
    #     return super(bienes_inmuebles, self).create(vals)
    #     self.bienes_numbien = vals

   



    
    _sql_constraints = [('bienes_numbien','unique(bienes_numbien,bienes_sedes_id)', 'El Número de Bien debe se único!')]
 
    _defaults = { 
         'sw_desin': False,
         'active': True }


    


# class remodelaciones(models.Model):
#     """Registro del tipo de remodelaciones del edificio"""
#     _name = 'remodelaciones'
#     _rec_name = 'remodelaciones_nombre'
#     remodelaciones_nombre = fields.Char(string='Descripción de la Remodelacion',size=200,required=True, help='Registra el Nombre del Tipo de Anexos del Inmueble')
#     remodelaciones_fecha =  fields.Date('Fecha de Remodelacion', size=8,help='Registra la Fecha de Remodelacion del Inmueble')   
#     remodelaciones_costo =  fields.Float(string='Costo de la Remodelación', help='Registra el Costo de la Remodelación')
#     bienes_inmuebles_id  =  fields.Many2one('bienes_inmuebles', string='Inmueble remodelado', size=3,required=True, help='Registra el Inmueble Remodelado')   
    


class clase_funcional_terr(models.Model):
    """Clasificacion funcional del terreno"""
    _name = 'clase_funcional_terr'
    _rec_name = 'clase_funcional_terr_nombre'

    clase_funcional_terr_codigo = fields.Char(string='Codigo del Tipo de Anexo',size=3,help='Registra el Codigo de la Clasificación Funcional del Terreno')
    clase_funcional_terr_nombre = fields.Char(string='Descripción de la Clasificacion',size=200,required=True, help='Registra el Nombre del Tipo de Anexos del Inmueble')
    bienes_inmuebles_id  =  fields.Many2one('bienes_inmuebles', string='Terreno Clasificado', size=3, help='Registra el Terreno Clacificado')   
    


class unidad_medida_terreno(models.Model):
    """Registra la Unidad de medida del Terreno"""
    _name = 'unidad_medida_terreno'
    _rec_name = 'unidad_medida_terreno_nombre'
    

    unidad_medida_terreno_codigo  = fields.Char(string='Codigo de la Unidad de Medida',size=6,required=True, help='Registra el Codigo de la Unidad de Medida')
    unidad_medida_terreno_nombre  = fields.Char(string='Nombre de la Unidad de Medida',size=100,required=True, help='Registra el Nombre de la Unidad de Medida')
    unidad_medida_terreno_simbolo = fields.Char(string='Simbolo de la Unidad de Medida',size=3,required=True, help='Registra el Simbolo de la Unidad de Medida')
    unidad_medida_terreno_tipo    = fields.Char(string='Tipo de la Unidad de Medida',size=3,required=True, help='Registra el Tipo de la Unidad de Medida')
    
    _sql_constraints = [('unidad_medida_terreno_codigo', 'unique(unidad_medida_terreno_codigo)', 'El Código debe se único!')]  
    _sql_constraints = [(' unidad_medida_terreno_nombre', 'unique(unidad_medida_terreno_nombre)', 'El Nombre debe se único!')]    




class unidad_medida_construccion(models.Model):
    """Registra la Unidad de medida de la  Construccion"""
    _name = 'unidad_medida_construccion'
    _rec_name = 'unidad_medida_construccion_nombre'
    

    unidad_medida_construccion_codigo  = fields.Char(string='Codigo de la Unidad de Medida',size=6,required=True, help='Registra el Codigo de la Unidad de Medida')
    unidad_medida_construccion_nombre  = fields.Char(string='Nombre de la Unidad de Medida',size=100,required=True, help='Registra el Nombre de la Unidad de Medida')
    unidad_medida_construccion_simbolo = fields.Char(string='Simbolo de la Unidad de Medida',size=3,required=True, help='Registra el Simbolo de la Unidad de Medida')
    unidad_medida_construccion_tipo    = fields.Char(string='Tipo de la Unidad de Medida',size=3,required=True, help='Registra el Tipo de la Unidad de Medida')
    



    _sql_constraints = [('unidad_medida_construccion_codigo', 'unique(unidad_medida_construccion_codigo)', 'El Código debe se único!')]  
    _sql_constraints = [(' unidad_medida_construccion_nombre', 'unique(unidad_medida_construccion_nombre)', 'El Nombre debe se único!')]    



class uso_inmueble(models.Model):
    """Registra el estatus de uso que tiene el Bien"""
    _name = 'uso_inmueble'
    #_rec_name = 'uso_inmueble_codigo'
    _rec_name = 'uso_inmueble_nombre'
    
    uso_inmueble_codigo = fields.Char(string='Codigo del Uso del Inmueble',size=3,required=True, help='Registra el Codigo de Uso del Inmueble')
    uso_inmueble_nombre = fields.Char(string='Nombre del Uso del Inmueble',size=40,required=True, help='Registra la Descripcion del Uso del Inmueble')

    
    _sql_constraints = [('uso_inmueble_codigo ', 'unique(uso_inmueble_codigo)', 'El Código debe se único!')]    
    _sql_constraints = [('uso_inmueble_nombre', 'unique(uso_inmueble_nombre)', 'El Nombre debe se único!')] 


class estado_ocupacion_inmueble(models.Model):
    """Registra el estatus de uso que tiene el Bien"""
    _name = 'estado_ocupacion_inmueble'
    #_rec_name = 'uso_inmueble_codigo'
    _rec_name = 'estado_ocupacion_inmueble_nombre'
    
    estado_ocupacion_inmueble_codigo = fields.Char(string='Codigo del Uso del Inmueble',size=3,required=True, help='Registra el Codigo de Uso del Inmueble')
    estado_ocupacion_inmueble_nombre = fields.Char(string='Nombre del Uso del Inmueble',size=40,required=True, help='Registra la Descripcion del Uso del Inmueble')

    
    _sql_constraints = [('estado_ocupacion_inmueble_codigo', 'unique(estado_ocupacion_inmueble_codigo)', 'El Código debe se único!')]    
    _sql_constraints = [('estado_ocupacion_inmueble_nombre', 'unique(estado_ocupacion_inmueble_nombre)', 'El Nombre debe se único!')] 
