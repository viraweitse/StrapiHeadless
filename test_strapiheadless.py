# test_strapiheadless.py
"""
Tests for StrapiHeadless module.
"""

import unittest
from strapiheadless import StrapiHeadless

class TestStrapiHeadless(unittest.TestCase):
    """Test cases for StrapiHeadless class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StrapiHeadless()
        self.assertIsInstance(instance, StrapiHeadless)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StrapiHeadless()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
