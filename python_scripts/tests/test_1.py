import unittest
import sys
import argparse
from os.path import dirname, abspath, join

# Add the parent directory to sys.path
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

# Import the function from batch_tester.py
from batch_tester import read_batch
from send_email import send_email

class TestBatchTester(unittest.TestCase):
    
    def test_read_batch(self):
        # Access the filename from command-line arguments
        filename = self.filename
        result = read_batch(filename)
        print("result:",result)
        
        if result:

            # Example usage
            subject = "Urgent: Data Error Detected"
            body = "Hi,I hope this message finds you well. \nI wanted to bring to your attention an error I encountered in the data.\n Please review the details at your earliest convenience and let me know if any action is needed.\nThank you!\n Best regards,\n\n(This is an automated message notifying you of a detected error in the data.)"
            email_sender = "gavriel@amiteam.net"
            email_password = "akmz mzqy okrc farh" # A token password ,Not you email password . 
            # email_receiver = "yakov@amiteam.net" # yakov@amiteam.net
            # send_email(subject, body, email_sender, email_password, email_receiver)
            print("email about the data was sent")

            email_sender = "gavriel@amiteam.net"
            email_receiver = "gavrielmn@gmail.com" 
            send_email(subject, body, email_sender, email_password, email_receiver)
            print("email about the data was sent")

        # Example assertion (replace with actual test logic)
        self.assertIsNotNone(result, "The batch file has error in the data.")

def main():
    parser = argparse.ArgumentParser(description='Run batch file tests.')
    parser.add_argument('filename', type=str, help='The path to the batch file to test')
    args = parser.parse_args()

    # Set the filename for the test
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestBatchTester)
    for test in test_suite:
        test.filename = args.filename

    unittest.TextTestRunner().run(test_suite)

if __name__ == '__main__':
    main()
