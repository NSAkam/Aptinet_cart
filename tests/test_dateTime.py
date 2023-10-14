import unittest
from scripts.Services.dateTime import DateTimeWorker, DateTime


class TestDateTime(unittest.TestCase):
    def setUp(self) -> None:
        self.datetime = DateTime()
    
    
    def test_update_signal(self):
        datetime_worker = DateTimeWorker()
        signal_emitted = False
    
        def update_slot(h, m, s):
            nonlocal signal_emitted
            signal_emitted = True
            self.assertEqual(h, datetime_worker.h)
            self.assertEqual(m, datetime_worker.m)
            self.assertEqual(s, datetime_worker.s)
            
        datetime_worker.update.connect(update_slot)
        datetime_worker.start()
        datetime_worker.sleep(3)
        datetime_worker.quit()
        datetime_worker.wait()
        self.assertTrue(signal_emitted)
    
    def test_setUpdatedTime(self):
        hh = 12
        mm = 34
        ss = 56
        self.datetime.setUpdatedTime(hh, mm, ss)
        self.assertEqual(self.datetime.h, hh)
        self.assertEqual(self.datetime.m, mm)
        self.assertEqual(self.datetime.s, ss)
        expected_time = f"{hh:12}:{mm:34}:{ss:56}"
        self.assertEqual(self.datetime.time, expected_time)
        
    def test_historyHandler(self):
        input_str = "21/7/5"
        self.datetime.historyHandler(input_str)
        expected_history = "210705"
        self.assertEqual(self.datetime.history, expected_history)

        
        
if __name__ == '__main__':
    unittest.main()