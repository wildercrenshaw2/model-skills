import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class SkillTests(unittest.TestCase):
    def test_four_skills_have_frontmatter_and_distinct_contracts(self):
        expected = {
            "image-generation": ["gpt-image-2", "/v1/images/generations", "max_references"],
            "video-generation": ["seedance-2.5", "/v1/videos/generations", "adaptive"],
            "minimax-h3-video": ["minimax-h3", "768p", "7,000"],
            "text-responses": ["gpt-6-sol", "/v1/responses", "function_call"],
        }
        actual = set()
        for directory, tokens in expected.items():
            path = ROOT / "skills" / directory / "SKILL.md"
            self.assertTrue(path.is_file())
            text = path.read_text()
            self.assertTrue(text.startswith("---\n"))
            self.assertRegex(text, r"(?m)^name: [a-z0-9-]+$")
            self.assertIn("description:", text)
            for token in tokens:
                self.assertIn(token, text)
            actual.add(directory)
        self.assertEqual(actual, set(expected))

    def test_no_obsolete_discovery_skill_remains(self):
        self.assertFalse((ROOT / "skills/model-discovery").exists())

    def test_readme_describes_all_four(self):
        text = (ROOT / "README.md").read_text()
        for name in ("GPT Image 2", "Seedance 2.5", "MiniMax H3", "GPT-6 Sol"):
            self.assertIn(name, text)


if __name__ == "__main__":
    unittest.main()
