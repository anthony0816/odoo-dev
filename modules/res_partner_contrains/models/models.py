from odoo import models, api, _
from odoo.exceptions import ValidationError


class ResPartnerConstrain(models.Model):
    _inherit ="res.partner"
    
    @api.constrains('email','phone')
    def check_unique_email_phone(self):
        for record in self:
            if record.email:
                existing_email = self.search([('email', '=', record.email),
                             ('id', '!=', record.id)
                             ], limit= 1)
                if existing_email :
                    raise ValidationError(
                        _('a contact with the same email its been register already')
                         )
            
            if record.phone:
                existing_phone = self.search([('phone','=', record.phone),
                                              ('id', '!=', record.id)],
                                             limit=1)
                if existing_phone:
                    raise ValidationError(
                        _('a contact with the same phone already exist')
                    )
            
                
