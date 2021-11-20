# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Tintuk Tomin(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Odoo Debranding - Frontend",
    'version': "13.0.1.3.3",
    'summary': """Odoo Frontend Debranding""",
    'description': """Frontend Debrand Odoo,Debranding, odoo13""",
    'live_test_url': 'https://www.youtube.com/watch?v=fYSPARjmYA4',
    'author': "Cybrosys Techno Solutions",
    'company': "Cybrosys Techno Solutions",
    'maintainer': "Cybrosys Techno Solutions",
    'website': "https://cybrosys.com/",
    'category': 'Tools',
    'depends': ['odoo-debrand-backend', 'website'],
    'data': [
        'views/views.xml',
    ],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
    'auto_install': True,
}
