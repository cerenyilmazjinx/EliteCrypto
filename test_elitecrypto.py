# test_elitecrypto.py
"""
Tests for EliteCrypto module.
"""

import unittest
from elitecrypto import EliteCrypto

class TestEliteCrypto(unittest.TestCase):
    """Test cases for EliteCrypto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EliteCrypto()
        self.assertIsInstance(instance, EliteCrypto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EliteCrypto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
