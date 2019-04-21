# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import Warning

class pos_coupons_setting(models.Model):
    _name = 'pos.coupons.setting'





    @api.one
    @api.constrains('min_coupan_value','max_coupan_value')
    def _check_amount(self):
    	if self.min_coupan_value >= self.max_coupan_value:
    		raise Warning(_("Minimum amount must be less than maximum amount"))
    	if self.max_coupan_value <= self.min_coupan_value:
    		raise Warning(_("Maximum amount must be greater than minimum amount")) 



    @api.model
    def create(self, vals):
        
        if self.search_count([('active','=',True)]) > 1:
            raise Warning(_('Allows only one activated Configuration of POS'))  
        else:
            return super(pos_coupons_setting,self).create(vals)

    name  = fields.Char('Name' ,default='Configuration for POS Gift Coupons')
    product_id  = fields.Many2one('product.product','Product', domain = [('type', '=', 'service')])
    min_coupan_value  =  fields.Float('Minimum Coupon Value')
    max_coupan_value  =  fields.Float('Maximum Coupon Value')
    max_exp_date  =  fields.Datetime('Maximum Expiry Date')
    #one_time_use =  fields.Boolean('(Redeem Coupon only if the order total is greater than the coupon value.)')
    #partially_use  = fields.Boolean('(User can partially use their Coupons.)')
    default_name  = fields.Char('Name')
    #default_validity = fields.Integer('Validity(in days)', default= -1)
    default_value  =  fields.Integer('Coupon Value')
    default_availability  = fields.Integer('Total Available', default= -1)
    active  =  fields.Boolean('Active')




	
	

