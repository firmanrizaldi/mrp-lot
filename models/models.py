from odoo import models, fields, api

class MrpLot(models.Model):
	_name = 'mrp.production'
	_inherit = 'mrp.production'

	@api.model
	def create(self, values):
		res = super (MrpLot,self).create(values)
		lot_data = {
			'name' : res.name,
			'product_id' : res.product_id.id
			}
		
		self.env['stock.production.lot'].create(lot_data)
		return res