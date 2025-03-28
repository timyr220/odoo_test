{
    'name': 'Lunch Recipe',
    'version': '12.0.1.0.0',
    'summary': 'Manage ingredients in lunch products',
    'depends': ['lunch'],
    'author': 'Your Name',
    'category': 'Lunch',
    'data': [
        'security/ir.model.access.csv',
        'views/lunch_product_views.xml',
        'views/lunch_ingredient_line_views.xml',
#        'wizard/lunch_order_wizard_views.xml',   # если делаешь визард
        'report/lunch_order_report.xml',
        'report/lunch_order_template.xml',
    ],
    'installable': True,
    'application': True,
}
