import unittest
import serial
from unittest.mock import patch, Mock
from scripts.Services.scanner import ScannerWorker


class TestScanner(unittest.TestCase):
    def setUp(self) -> None:
        self.scanner = ScannerWorker()
    
    def test_outOfLogic(self):
        self.scanner.outOfLogic()
        self.assertTrue(self.scanner.out_of_logic)
        
    @patch('serial.Serial')
    def test_serial_connection(self, mock_serial):
        ScannerWorker()
        mock_serial.assert_called_once_with(
            "/dev/ttyS0",
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
           

        
if __name__ == '__main__':
    unittest.main()