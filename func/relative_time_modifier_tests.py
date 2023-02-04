from func import relative_time_modifier
from func.relative_time_modifier import RelativeTimeModifier
from datetime import datetime
import unittest
from mock import patch, Mock

class RelativeTimeModifierTests(unittest.TestCase):
    
    @patch.object(relative_time_modifier, 'datetime', Mock(wraps=datetime))
    def test_addition(self):
        relative_time_modifier.datetime.utcnow.return_value = datetime(1970, 1, 1)
        test_case = 'now()+1y+2mon+3d+4h+5m+6s'
        expected = datetime(1971, 3, 4, 4, 5, 6)
        
        actual = RelativeTimeModifier.parse(test_case)
        
        self.assertEqual(expected, actual)

    @patch.object(relative_time_modifier, 'datetime', Mock(wraps=datetime))
    def test_subtraction(self):
        relative_time_modifier.datetime.utcnow.return_value = datetime(1970, 1, 1)
        test_case = 'now()-3y-6mon-3d-12h-45m-64s'
        expected = datetime(1966, 6, 27, 11, 13, 56)
        
        actual = RelativeTimeModifier.parse(test_case)
        
        self.assertEqual(expected, actual)


    @patch.object(relative_time_modifier, 'datetime', Mock(wraps=datetime))
    def test_snapTo(self):
        relative_time_modifier.datetime.utcnow.return_value = datetime(2023, 2, 4, 22, 37, 45)
        
        # snap to each unit of time
        test_cases = [
            ( 'now()@y', datetime(2023, 1, 1, 0, 0, 0) ),
            ( 'now()@mon', datetime(2023, 2, 1, 0, 0, 0)),
            ( 'now()@d', datetime(2023, 2, 4, 0, 0, 0)),
            ( 'now()@h', datetime(2023, 2, 4, 22, 0, 0)),
            ( 'now()@m', datetime(2023, 2, 4, 22, 37, 0)),
            ( 'now()@s', datetime(2023, 2, 4, 22, 37, 45))
        ]

        for (input, expected) in test_cases:
            actual = RelativeTimeModifier.parse(input)
            self.assertEqual(expected, actual)

    @patch.object(relative_time_modifier, 'datetime', Mock(wraps=datetime))
    def test_mixedOperations(self):
        relative_time_modifier.datetime.utcnow.return_value = datetime(2023, 2, 4, 22, 37, 45)
        
        test_cases = [
            # order of operation is important
            ( 'now()@y+1mon', datetime(2023, 2, 1, 0, 0, 0) ),
            ( 'now()+1mon@y', datetime(2023, 1, 1, 0, 0, 0) ),
            ( 'now()-2mon@y', datetime(2022, 1, 1, 0, 0, 0) ),
            ( 'now()+90d@mon', datetime(2023, 5, 1, 0, 0, 0) ),
            ( 'now()@m+86400s', datetime(2023, 2, 5, 22, 37, 0) ),
        ]

        for (input, expected) in test_cases:
            actual = RelativeTimeModifier.parse(input)
            self.assertEqual(expected, actual)

    def test_parseOnlyAcceptsStrings(self):
        test_cases = [ 1, True, { } ]
        for test_case in test_cases:
            self.assertRaises(TypeError, RelativeTimeModifier.parse, test_case)

    def test_parseOnlyAcceptsWellFormattedStrings(self):
        test_cases = [ 
            '1970-01-01@d',
            'now()@d+1d-3y+12mo'
        ]
        for test_case in test_cases:
            self.assertRaises(ValueError, RelativeTimeModifier.parse, test_case)

if __name__ == '__main__':
    unittest.main()