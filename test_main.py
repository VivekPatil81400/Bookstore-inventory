import unittest
import main

class Test_is_valid_cin(unittest.TestCase):
    def test_length(self):
        self.assertFalse(main.is_valid_cin('1707224424'))
        self.assertFalse(main.is_valid_cin('173454546317224424'))

    def test_publication_type(self):
        self.assertFalse(main.is_valid_cin('10000372214424'))
        self.assertFalse(main.is_valid_cin('47100551007975'))


    def test_checksum(self):
        self.assertFalse(main.is_valid_cin('42100551007945')) 
        self.assertFalse(main.is_valid_cin('17000372214456'))
    
    def test_all_int(self):
        self.assertFalse(main.is_valid_cin('42100abc007945'))

class Test_calculate_inventory(unittest.TestCase):
    def test_start_inventory_cin(self):
        start_inventory = {'17000372214424':'10',
        }
        self.assertTrue(main.is_valid_cin('17000372214424'))

    def test_transaction_log_type(self):
        transaction_log = """17000372214424 INCOMING 9
        17000372214424 OUTGOING 1"""
        self.assertEqual(type(transaction_log), str)

    def test_book_count(self):
        start_inventory = {'17000372214424':'5'}
        transaction_log = """17000372214424 OUTGOING 6"""
        self.assertEqual(main.calculate_inventory(start_inventory,transaction_log), "Negative quantity of a stock is NOT possible, Kindly check.")