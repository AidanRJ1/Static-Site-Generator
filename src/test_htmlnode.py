import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
	def test_props_to_html(self):
		node = HtmlNode("a", "This is text", ["node", "node1"], {"href": "https://www.google.com", "target": "_blank"})
		expected = ' href="https://www.google.com" target="_blank"'
		self.assertEqual(node.props_to_html(), expected)

	def test_html_repr(self):
		node = HtmlNode("a", "This is text", ["node", "node1"], {"href": "https://www.google.com", "target": "_blank"})
		expected = "HtmlNode(a, This is text, ['node', 'node1'], {'href': 'https://www.google.com', 'target': '_blank'})"
		self.assertEqual(node.__repr__(), expected)

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Hello, world!", {"href": "https://www.boot.dev", "target": "_blank"})
		self.assertEqual(node.to_html(), '<a href="https://www.boot.dev" target="_blank">Hello, world!</a>')

	def test_leaf_to_html_no_tag(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")

	def test_leaf_repr(self):
		node = LeafNode("a", "Hello, world!", {"href": "https://www.boot.dev", "target": "_blank"})
		expected = "LeafNode(a, Hello, world!, {'href': 'https://www.boot.dev', 'target': '_blank'})"
		self.assertEqual(node.__repr__(), expected)

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		expected = "<div><span>child</span></div>"
		self.assertEqual(parent_node.to_html(), expected)

	def test_to_html_with_grandchildren(self):	
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		expected = "<div><span><b>grandchild</b></span></div>"
		self.assertEqual(parent_node.to_html(), expected)

	def test_to_html_many_children(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
		self.assertEqual(node.to_html(), expected)

	def test_headings(self):
		node = ParentNode(
			"h2",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)	
		expected = "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
		self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()