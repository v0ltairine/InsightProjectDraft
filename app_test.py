from app import pick_role_model
import unittest

#def fun(x):
 #   return x + 1

#class MyTest(unittest.TestCase):
 #   def test(self):
  #      self.assertEqual(fun(3), 4)
  
class AppTest(unittest.TestCase):
    def test_pick_role_model(self):
        self.assertEqual(pick_role_model("biology", "embroidery", "pittsburgh"), "Kathleen C. Allen")
        self.assertEqual(pick_role_model("biology", "embroidery", "los_angeles"), "Samantha Baker")
        self.assertEqual(pick_role_model("biology", "archery", "pittsburgh"), "Katrina A. Brown")
        self.assertEqual(pick_role_model("biology", "archery", "los_angeles"), "Sally Jensen")
        self.assertEqual(pick_role_model("math", "embroidery", "pittsburgh"), "Vanessa Corday")
        self.assertEqual(pick_role_model("math", "archery", "pittsburgh"), "Mariah Carnegie")
        self.assertEqual(pick_role_model("math", "embroidery", "los_angeles"), "Helen Swanson")
        self.assertEqual(pick_role_model("math", "archery", "los_angeles"), "Dorothy M. Smith")
        self.assertRaises(Exception, pick_role_model, "spider", "cat", "mouse")

if __name__ == '__main__':
    unittest.main()
         