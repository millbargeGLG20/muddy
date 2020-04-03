from muddy import app
import unittest 

#Test Return Code
#Test Returned Data

class FlaskBookshelfTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_muddy_status_code(self):
        result = self.app.get('/test/muddy/') 
        self.assertEqual(result.status_code, 200) 

    def test_muddy_data(self):
        result = self.app.get('/test/muddy/') 
        self.assertEqual(result.data, b'MUDDY')

    def test_not_muddy_status_code(self):
        result = self.app.get('/test/notmuddy/') 
        self.assertEqual(result.status_code, 200) 

    def test_not_muddy_data(self):
        result = self.app.get('/test/notmuddy/') 
        self.assertEqual(result.data, b'NOT MUDDY')
    
if __name__ == '__main__':
    unittest.main()