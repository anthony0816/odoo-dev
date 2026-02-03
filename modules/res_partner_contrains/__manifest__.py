{
    'name': "res_partner_contrains",

    'summary': "Ensure email and phone unique for all contacts",

    'description': """
Adds validation constraints to res.partner so that email and phone
must be unique across all contacts.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [],
    
    'installable': True, 
    'application': False,
}

