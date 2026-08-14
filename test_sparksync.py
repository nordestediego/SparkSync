# test_sparksync.py
"""
Tests for SparkSync module.
"""

import unittest
from sparksync import SparkSync

class TestSparkSync(unittest.TestCase):
    """Test cases for SparkSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkSync()
        self.assertIsInstance(instance, SparkSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
