{
    'name': 'Geotagging Odoo',
    'version': '1.0',
    'summary': 'Geotagging Odoo',
    'sequence': 1,
    'description': """Geotagging Odoo""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'web_google_maps',
        'web',
        # 'web_map',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/geotagging.xml',
        'views/maps.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'geotagging_odoo/static/**/*',
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
