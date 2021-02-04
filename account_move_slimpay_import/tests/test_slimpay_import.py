# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.modules import get_resource_path

from odoo.addons.account_move_base_import.tests import common


class TestAccountMoveSlimpayImport(common.TestAccountMoveBaseImport):

    def setUp(self):
        super().setUp()
        self.journal.import_type = 'slimpay'

    def test_slimpay_import(self):
        file_name = get_resource_path(
            'account_move_slimpay_import',
            'tests',
            'data',
            'statement.csv'
        )
        import ipdb; ipdb.set_trace()
        move = self._import_file(file_name)
        pass
