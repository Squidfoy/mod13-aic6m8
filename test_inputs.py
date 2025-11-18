import unittest
import main
from datetime import datetime
import re

class TestInputs(unittest.TestCase):
    def test_symbol_capitalized(self):
        #valid: all uppercase
        valid_symbols = ["AAPL", "GOOGL", "IBM", "A", "MSFT"]
        for symbol in valid_symbols:
            self.assertTrue(symbol.isupper())
            self.assertTrue(symbol.isalpha())
        
        #invalid: lowercase or moxed case
        invalid_symbols = ["aapl", "Aapl", "AaPl", "aPPL"]
        for symbol in invalid_symbols:
            self.assertFalse(symbol.isupper())
                

    def test_symbol_length(self):
        #make sure symbol length isbetween 1-7 characters
        #valid lengths
        valid_symbols = ["A", "AB", "ABC", "AAPL", "GOOGL", "ABCDEF", "ABCDEFG"]
        for symbol in valid_symbols:
            self.assertTrue(1 <= len(symbol) <= 7)
            self.assertTrue(symbol.isalpha())
        
        #invalid lengths
        self.assertFalse(len("") >= 1 and len("") <= 7)  # empty
        self.assertFalse(len("ABCDEFGH") <= 7)
        

    def test_chart_type(self):
        #make sure chart type is one numeric character, 1-2
        #valid chart types
        self.assertTrue(self.validate_chart_type("1"))
        self.assertTrue(self.validate_chart_type("2"))
        
        #invalid: other numbers, non numeric, wrong length
        self.assertFalse(self.validate_chart_type("0"))
        self.assertFalse(self.validate_chart_type("3"))
        self.assertFalse(self.validate_chart_type("5"))
        self.assertFalse(self.validate_chart_type("a"))
        self.assertFalse(self.validate_chart_type("GOOGL"))
        self.assertFalse(self.validate_chart_type(""))
        self.assertFalse(self.validate_chart_type("15"))

    def test_time_series(self):
        #make sure time series is one numeric character, 1-4
        #valid time series types
        self.assertTrue(self.validate_time_series("1"))  
        self.assertTrue(self.validate_time_series("2"))  
        self.assertTrue(self.validate_time_series("3"))  
        self.assertTrue(self.validate_time_series("4"))  
        
        #invalid: other numbers, non numeric, wrong length
        self.assertFalse(self.validate_time_series("0"))  
        self.assertFalse(self.validate_time_series("5"))  
        self.assertFalse(self.validate_time_series("9"))  
        self.assertFalse(self.validate_time_series("a"))  
        self.assertFalse(self.validate_time_series("GOOGL"))  
        self.assertFalse(self.validate_time_series(""))  
        self.assertFalse(self.validate_time_series("15"))

    def test_start_date(self):
        #make sure start date is in YYYY-MM-DD format
        #valid formats
        self.assertTrue(self.validate_date("2024-01-01"))
        self.assertTrue(self.validate_date("2023-12-31"))
        self.assertTrue(self.validate_date("2020-06-15"))
        
        #invalid formats
        self.assertFalse(self.validate_date("01-01-2024"))    
        self.assertFalse(self.validate_date("2024/01/01"))    
        self.assertFalse(self.validate_date("2024-1-1"))      
        self.assertFalse(self.validate_date("24-01-01"))      
        self.assertFalse(self.validate_date("not-a-date"))
        self.assertFalse(self.validate_date(""))

    def test_end_date(self):
        #make sure end date is in YYYY-MM-DD format
        #valid formats
        self.assertTrue(self.validate_date("2024-01-01"))
        self.assertTrue(self.validate_date("2023-12-31"))
        self.assertTrue(self.validate_date("2020-06-15"))
        
        #invalid formats
        self.assertFalse(self.validate_date("01-01-2024"))    
        self.assertFalse(self.validate_date("2024/01/01"))    
        self.assertFalse(self.validate_date("2024-1-1"))      
        self.assertFalse(self.validate_date("24-01-01"))      
        self.assertFalse(self.validate_date("not-a-date"))
        self.assertFalse(self.validate_date(""))

#since the functions in main.py ask for user input, i will create validation functions here to test the inputs
    def validate_chart_type(self, chart_type):
        if len(chart_type) != 1:
            return False
        if not chart_type.isdigit():
            return False
        if chart_type not in ["1", "2"]:
            return False
        return True

    
    def validate_time_series(self, time_series):
        if len(time_series) != 1:
            return False
        if not time_series.isdigit():
            return False
        if time_series not in ["1", "2", "3", "4"]:
            return False
        return True

    def validate_date(self, date_string):

        #check if matches YYYY-MM-DD pattern
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_string):
            return False
        


if __name__ == '__main__':
    unittest.main()
