# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Theme',
    'summary': 'Customize theme for Odoo',
    'description': """
        This module add functionality to customize Odoo interface
    """,
    'author': 'M Rizki Alif R',
    'website': 'https://www.linkedin.com/in/mrizkialifr/',
    'category': 'Theme',
    'license': 'LGPL-3',
    'version': '0.1',
    'depends': ["base_setup"],
    'sequence': 15,
    'data': [
        'views/assets.xml',
    ],
    "application": False,
    "installable": True,
    "auto_install": True,
}
