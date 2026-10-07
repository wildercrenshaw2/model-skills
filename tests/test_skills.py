import pathlib,re,unittest
class T(unittest.TestCase):
 def test_frontmatter(self):
  for p in pathlib.Path("skills").glob("*/SKILL.md"):
   s=p.read_text(); self.assertTrue(s.startswith("---\n")); self.assertRegex(s,r"description:")
if __name__=="__main__":unittest.main()
