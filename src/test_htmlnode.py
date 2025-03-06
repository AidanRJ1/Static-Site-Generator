import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
	def test_props_to_html(self):
		tests = [
			[ 
				HtmlNode("a", "This is text", ["node", "node1"], {"href": "https://www.google.com", "target": "_blank"}),
				' href="https://www.google.com" target="_blank"',
			],
			[
				HtmlNode("a", "This is text", ["node", "node1"], {"href": "https://www.boot.dev"}),
				' href="https://www.boot.dev"',
			],
			[
				HtmlNode("h1", "This is text", ["node", "node1"], {"class": "heading, flex"}),
				' class="heading, flex"',
			],
			
		]
		
		for test in tests:
			result = test[0].props_to_html()
			self.assertEqual(result, test[1])

if __name__ == "__main__":
    unittest.main()