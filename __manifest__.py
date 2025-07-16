{
    'name': 'Advanced Customer Sales Flow',
    'version': '1.0',
    'summary': 'Enhance customer data with sectors and loyalty scoring',
    'description': """
This module extends the customer model (res.partner) with additional fields to support advanced sales workflows.

Key Features:
  -Sector Classification: Categorize each customer as Public, Private, or NGO.
  -Loyalty Score: Track customer loyalty using a numerical score.
  -Better Segmentation: Help sales teams filter and prioritize clients based on sector and loyalty.
  -Supports Targeting & Analytics: Useful for reporting, targeted campaigns, and sales performance analysis.
    """,
    'category': 'Sales',
    'author': 'Hany Youssef',
    'depends': ['base','sale','stock'],
    'data': [
        'views/partner_menu.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',

    ],
    'installable': True,
    'application': False,
}
