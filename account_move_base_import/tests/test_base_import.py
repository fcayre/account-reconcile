# Copyright 2011-2016 Akretion
# Copyright 2011-2019 Camptocamp SA
# Copyright 2013 Savoir-faire Linux
# Copyright 2014 ACSONE SA/NV
# Copyright 2021 Commown
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from operator import attrgetter

from odoo import fields
from odoo.modules import get_resource_path

from . import common


class TestCodaImport(common.TestAccountMoveBaseImport):

    def test_simple_xls(self):
        """Test import from xls
        """
        file_name = get_resource_path(
            'account_move_base_import',
            'tests',
            'data',
            'statement.xls'
        )
        move = self._import_file(file_name)
        self._validate_imported_move(move)

    def test_simple_csv(self):
        """Test import from csv
        """
        file_name = get_resource_path(
            'account_move_base_import',
            'tests',
            'data',
            'statement.csv'
        )
        move = self._import_file(file_name)
        self._validate_imported_move(move)

    def _validate_imported_move(self, move):
        self.assertEqual("/", move.name)
        self.assertEqual(5, len(move.line_ids))
        move_line = sorted(move.line_ids,
                           key=attrgetter('date_maturity'))[2]
        # common infos
        self.assertEqual(
            move_line.date_maturity, fields.Date.from_string('2011-03-07')
        )
        self.assertEqual(move_line.credit, 118.4)
        self.assertEqual(move_line.name, "label a")
