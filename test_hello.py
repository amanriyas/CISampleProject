from hello import greet_user

class TestGreetUser(unittest.TestCase):
  def test_greet_user(self):
    self.assertEqual(greet_user("Alice"), "Hello, Alice!")