import unittest
from extract import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))
		

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
	
	def test_Zeroindex (self):
		self.assertEqual('r1551925', commits[0]['revision'])
		
	
	def check_author(self):
		self.assertEqual('Thomas', commits[0]['author'])	
        self.assertEqual('Jimmy', commits[420]['author'])
	
	def check_indexPos(self):
		self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],commits[20]['changed_path'])

if __name__ == '__main__':
    unittest.main()
