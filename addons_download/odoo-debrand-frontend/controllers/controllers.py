# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(
#    <https://www.cybrosys.com>).
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

import base64
import functools
import io
import json

from odoo.http import request

import jinja2
import odoo
import os
import sys
from odoo import http
from odoo.addons.web.controllers import main
from odoo.addons.web.controllers.main import Binary
from odoo.addons.web.controllers.main import Database

if hasattr(sys, 'frozen'):
    # When running on compiled windows binary, we don't have access to
	# package loader.
    path = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..', 'views'))
    loader = jinja2.FileSystemLoader(path)
else:
    loader = jinja2.PackageLoader('odoo.addons.odoo-debrand-frontend', "views")
env = main.jinja2.Environment(loader=loader, autoescape=True)
env.filters["json"] = json.dumps
db_monodb = http.db_monodb
DBNAME_PATTERN = '^[a-zA-Z0-9][a-zA-Z0-9_.-]+$'

class OdooDebrand(Database):

    def _render_template(self, **d):

        d.setdefault('manage', True)
        d['insecure'] = odoo.tools.config.verify_admin_password('admin')
        d['list_db'] = odoo.tools.config['list_db']
        d['langs'] = odoo.service.db.exp_list_lang()
        d['countries'] = odoo.service.db.exp_list_countries()
        d['pattern'] = DBNAME_PATTERN
        website_id = request.env['website'].sudo().search([])
        d['website_name'] = website_id and website_id[0].name or ''
        d['company_name'] = website_id and website_id[0].company_id.name or ''
        d['favicon'] = website_id and website_id[0].favicon_url or ''
        d['company_logo_url'] = website_id and website_id[
            0].company_logo_url or ''

        # databases list
        d['databases'] = []
        try:
            d['databases'] = http.db_list()
            d['incompatible_databases'] = odoo.service.db.list_db_incompatible(
                d['databases'])
        except odoo.exceptions.AccessDenied:
            monodb = db_monodb()
            if monodb:
                d['databases'] = [monodb]
        return env.get_template("database_manager_extend.html").render(d)
