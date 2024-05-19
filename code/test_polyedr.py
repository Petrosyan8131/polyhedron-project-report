import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_sum01(self):
        self.assertEqual(Polyedr('data/box.geom').edges_lenght(), 12.0)

    def test_sum02(self):
        self.assertEqual(Polyedr('data/ccc.geom').edges_lenght(), 30.0)

    def test_sum03(self):
        a = 35.29536857
        self.assertAlmostEqual(Polyedr('data/king.geom').edges_lenght(), a)

    def test_sum04(self):
        a = 2324.05376815
        self.assertAlmostEqual(Polyedr('data/babem.geom').edges_lenght(), a)

    def test_sum05(self):
        b = 976.4371654314
        self.assertAlmostEqual(Polyedr('data/cow.geom').edges_lenght(), b)

    def test_sum06(self):
        self.assertAlmostEqual(Polyedr('data/new_box.geom').edges_lenght(), 0)
