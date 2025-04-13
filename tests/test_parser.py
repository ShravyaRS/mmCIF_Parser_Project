import unittest
from mmcif_parser import mmCIFParser

class TestmmCIFParser(unittest.TestCase):
    def test_parse_file(self):
        parser = mmCIFParser("data/example.cif")
        self.assertTrue(parser.data_block is not None)

if __name__ == "__main__":
    unittest.main()
