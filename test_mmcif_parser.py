import unittest
from mmcif_parser import parse_mmcif

class TestParser(unittest.TestCase):
    def test_parse_headers(self):
        result = parse_mmcif("example.cif")
        self.assertIn("_entry.id", result)
        print("✅ File parsed successfully!")  # ✅ This will print only if test passes

if __name__ == '__main__':
    unittest.main()
