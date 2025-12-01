"""
Comprehensive unit tests for buggy_percentage.py

This test suite covers:
1. Syntax validation (the file currently has invalid Python syntax)
2. Import behavior (should fail due to syntax errors)
3. Expected behavior if the bug were fixed (percentage calculations)
4. Edge cases and error handling for a proper percentage function
"""

import pytest
import sys
import ast
from pathlib import Path


class TestBuggyPercentageSyntax:
    """Test suite for validating the syntax issues in buggy_percentage.py"""
    
    def test_file_exists(self):
        """Verify that buggy_percentage.py file exists"""
        file_path = Path(__file__).parent / "buggy_percentage.py"
        assert file_path.exists(), "buggy_percentage.py should exist"
    
    def test_file_has_invalid_syntax(self):
        """Verify that the file contains invalid Python syntax"""
        file_path = Path(__file__).parent / "buggy_percentage.py"
        with open(file_path, 'r') as f:
            content = f.read()
        
        # The file should not be valid Python code
        with pytest.raises(SyntaxError):
            ast.parse(content)
    
    def test_file_content_structure(self):
        """Verify the specific invalid content in the file"""
        file_path = Path(__file__).parent / "buggy_percentage.py"
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # Check that file has exactly 2 lines
        assert len(lines) == 2, "File should have exactly 2 lines"
        
        # Check first line contains just '%'
        assert lines[0].strip() == '%', "First line should contain only '%'"
        
        # Check second line contains just '0'
        assert lines[1].strip() == '0', "Second line should contain only '0'"
    
    def test_cannot_import_module(self):
        """Verify that importing the module raises SyntaxError"""
        with pytest.raises(SyntaxError):
            import buggy_percentage
    
    def test_cannot_execute_as_script(self):
        """Verify that executing the file as a script fails"""
        import subprocess
        file_path = Path(__file__).parent / "buggy_percentage.py"
        
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            text=True
        )
        
        # Should have non-zero exit code due to syntax error
        assert result.returncode != 0, "Execution should fail with syntax error"
        assert "SyntaxError" in result.stderr or "invalid syntax" in result.stderr.lower()


class TestPercentageFunctionIfFixed:
    """
    Test suite for expected behavior if buggy_percentage.py were fixed.
    These tests describe what a proper percentage function should do.
    """
    
    @pytest.fixture
    def percentage_function(self):
        """Fixture providing a correct percentage implementation"""
        def percentage(value, total):
            """Calculate percentage: (value / total) * 100"""
            if total == 0:
                raise ValueError("Total cannot be zero")
            return (value / total) * 100
        return percentage
    
    def test_basic_percentage_calculation(self, percentage_function):
        """Test basic percentage calculations"""
        assert percentage_function(50, 100) == 50.0
        assert percentage_function(25, 100) == 25.0
        assert percentage_function(1, 4) == 25.0
        assert percentage_function(3, 4) == 75.0
    
    def test_percentage_greater_than_100(self, percentage_function):
        """Test percentages that exceed 100%"""
        assert percentage_function(150, 100) == 150.0
        assert percentage_function(200, 100) == 200.0
        assert percentage_function(5, 4) == 125.0
    
    def test_percentage_with_zero_value(self, percentage_function):
        """Test percentage when value is zero"""
        assert percentage_function(0, 100) == 0.0
        assert percentage_function(0, 50) == 0.0
        assert percentage_function(0, 1) == 0.0
    
    def test_percentage_with_zero_total_raises_error(self, percentage_function):
        """Test that division by zero is handled properly"""
        with pytest.raises(ValueError, match="Total cannot be zero"):
            percentage_function(50, 0)
        
        with pytest.raises(ValueError, match="Total cannot be zero"):
            percentage_function(0, 0)
    
    def test_percentage_with_negative_numbers(self, percentage_function):
        """Test percentage calculations with negative numbers"""
        assert percentage_function(-50, 100) == -50.0
        assert percentage_function(50, -100) == -50.0
        assert percentage_function(-50, -100) == 50.0
    
    def test_percentage_with_floats(self, percentage_function):
        """Test percentage calculations with floating point numbers"""
        assert percentage_function(33.33, 100) == pytest.approx(33.33, rel=1e-2)
        assert percentage_function(2.5, 10) == 25.0
        assert percentage_function(0.5, 2) == 25.0
    
    def test_percentage_with_very_small_numbers(self, percentage_function):
        """Test percentage with very small numbers"""
        result = percentage_function(0.001, 100)
        assert result == pytest.approx(0.001, rel=1e-6)
        
        result = percentage_function(1e-10, 1)
        assert result == pytest.approx(1e-8, rel=1e-9)
    
    def test_percentage_with_very_large_numbers(self, percentage_function):
        """Test percentage with very large numbers"""
        assert percentage_function(1e10, 1e12) == pytest.approx(1.0, rel=1e-6)
        assert percentage_function(5e6, 1e7) == pytest.approx(50.0, rel=1e-6)
    
    def test_percentage_precision(self, percentage_function):
        """Test that percentage maintains reasonable precision"""
        result = percentage_function(1, 3)
        assert result == pytest.approx(33.333333, rel=1e-5)
        
        result = percentage_function(2, 3)
        assert result == pytest.approx(66.666667, rel=1e-5)
    
    def test_percentage_return_type(self, percentage_function):
        """Test that percentage returns a numeric type"""
        result = percentage_function(50, 100)
        assert isinstance(result, (int, float))
    
    def test_percentage_with_same_values(self, percentage_function):
        """Test percentage when value equals total (should be 100%)"""
        assert percentage_function(100, 100) == 100.0
        assert percentage_function(50, 50) == 100.0
        assert percentage_function(1, 1) == 100.0


class TestPercentageAlternativeImplementations:
    """Test alternative percentage calculation implementations"""
    
    def test_percentage_as_decimal(self):
        """Test percentage calculation returning decimal (0-1 range)"""
        def percentage_decimal(value, total):
            if total == 0:
                raise ValueError("Total cannot be zero")
            return value / total
        
        assert percentage_decimal(50, 100) == 0.5
        assert percentage_decimal(25, 100) == 0.25
        assert percentage_decimal(1, 4) == 0.25
    
    def test_percentage_with_rounding(self):
        """Test percentage calculation with rounding"""
        def percentage_rounded(value, total, decimals=2):
            if total == 0:
                raise ValueError("Total cannot be zero")
            return round((value / total) * 100, decimals)
        
        assert percentage_rounded(1, 3) == 33.33
        assert percentage_rounded(2, 3) == 66.67
        assert percentage_rounded(1, 7, decimals=1) == 14.3
    
    def test_percentage_formatted_string(self):
        """Test percentage calculation returning formatted string"""
        def percentage_string(value, total):
            if total == 0:
                raise ValueError("Total cannot be zero")
            pct = (value / total) * 100
            return f"{pct:.2f}%"
        
        assert percentage_string(50, 100) == "50.00%"
        assert percentage_string(1, 3) == "33.33%"
        assert percentage_string(2, 3) == "66.67%"


class TestPercentageEdgeCases:
    """Test edge cases and boundary conditions for percentage calculations"""
    
    @pytest.fixture
    def percentage_function(self):
        """Fixture providing a correct percentage implementation"""
        def percentage(value, total):
            if total == 0:
                raise ValueError("Total cannot be zero")
            return (value / total) * 100
        return percentage
    
    def test_percentage_with_infinity(self, percentage_function):
        """Test behavior with infinity values"""
        assert percentage_function(float('inf'), 100) == float('inf')
        
        # Infinity divided by infinity is NaN
        result = percentage_function(float('inf'), float('inf'))
        assert result != result  # NaN != NaN
    
    def test_percentage_with_none_raises_error(self, percentage_function):
        """Test that None values raise appropriate errors"""
        with pytest.raises(TypeError):
            percentage_function(None, 100)
        
        with pytest.raises(TypeError):
            percentage_function(50, None)
    
    def test_percentage_with_string_raises_error(self, percentage_function):
        """Test that string values raise appropriate errors"""
        with pytest.raises(TypeError):
            percentage_function("50", 100)
        
        with pytest.raises(TypeError):
            percentage_function(50, "100")
    
    def test_percentage_with_list_raises_error(self, percentage_function):
        """Test that list values raise appropriate errors"""
        with pytest.raises(TypeError):
            percentage_function([50], 100)
        
        with pytest.raises(TypeError):
            percentage_function(50, [100])
    
    def test_percentage_commutative_property(self, percentage_function):
        """Test that percentage is not commutative (order matters)"""
        result1 = percentage_function(25, 100)
        result2 = percentage_function(100, 25)
        
        assert result1 != result2
        assert result1 == 25.0
        assert result2 == 400.0


class TestPercentageIntegration:
    """Integration tests for percentage calculations in real-world scenarios"""
    
    @pytest.fixture
    def percentage_function(self):
        """Fixture providing a correct percentage implementation"""
        def percentage(value, total):
            if total == 0:
                raise ValueError("Total cannot be zero")
            return (value / total) * 100
        return percentage
    
    def test_percentage_in_grade_calculation(self, percentage_function):
        """Test percentage for calculating exam grades"""
        # Student scored 85 out of 100
        grade = percentage_function(85, 100)
        assert grade == 85.0
        
        # Student scored 42 out of 50
        grade = percentage_function(42, 50)
        assert grade == 84.0
    
    def test_percentage_in_statistics(self, percentage_function):
        """Test percentage for statistical calculations"""
        # 45 people out of 200 surveyed
        participation = percentage_function(45, 200)
        assert participation == 22.5
        
        # 3 defective items out of 1000
        defect_rate = percentage_function(3, 1000)
        assert defect_rate == 0.3
    
    def test_percentage_in_financial_calculations(self, percentage_function):
        """Test percentage for financial scenarios"""
        # Interest: $50 interest on $1000 principal
        interest_rate = percentage_function(50, 1000)
        assert interest_rate == 5.0
        
        # Discount: $20 off on $100 item
        discount = percentage_function(20, 100)
        assert discount == 20.0
    
    def test_percentage_change_calculation(self, percentage_function):
        """Test percentage change between two values"""
        # Price increased from 50 to 75
        old_price = 50
        new_price = 75
        change = new_price - old_price
        percentage_change = percentage_function(change, old_price)
        assert percentage_change == 50.0
        
        # Price decreased from 100 to 80
        old_price = 100
        new_price = 80
        change = new_price - old_price
        percentage_change = percentage_function(change, old_price)
        assert percentage_change == -20.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])