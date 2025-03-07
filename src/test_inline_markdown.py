import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class SplitNodesDelimiter(unittest.TestCase):
	def test(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		expected = [
			[
			    TextNode("This is text with a ", TextType.TEXT),
			    TextNode("code block", TextType.CODE),
			    TextNode(" word", TextType.TEXT),
			],
		]
		self.assertEqual(new_nodes, expected)

class ExtractMarkdown(unittest.TestCase):
	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
		    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
		self.assertListEqual(matches, expected)

	def test_extract_markdown_images_multiple(self):
		matches = extract_markdown_images(
		    "This is text with two ![image](https://i.imgur.com/zjjcJKZ.png) and ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")]
		self.assertListEqual(matches, expected)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
		    "This is text with a link [to boot dev](https://www.boot.dev)"
		)
		expected = [("to boot dev", "https://www.boot.dev")]
		self.assertListEqual(matches, expected)

	def test_extract_markdown_links_multiple(self):
		matches = extract_markdown_links(
		    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		)
		expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
		self.assertListEqual(matches, expected)

	#
	def test_split_image(self):
		matches = split_nodes_image([TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)])
		expected = [
			TextNode("This is text with an ", TextType.TEXT, None),
			TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
		]
		self.assertListEqual(matches, expected)

	def test_split_image_single(self):
		matches = split_nodes_image([TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)])
		expected = [
			TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
		]
		self.assertListEqual(matches, expected)

	def test_split_images(self):
		matches = split_nodes_image([TextNode("This is text with three images: ![image](https://i.imgur.com/zjjcJKZ.png), ![image2](https://i.imgur.com/zjjcKKZ.png) and ![image3](https://i.imgur.com/zjjcZKZ.png), thats it.", TextType.TEXT)])
		expected = [
			TextNode("This is text with three images: ", TextType.TEXT, None),
			TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			TextNode(", ", TextType.TEXT, None),
			TextNode("image2", TextType.IMAGE, "https://i.imgur.com/zjjcKKZ.png"),
			TextNode(" and ", TextType.TEXT, None),
			TextNode("image3", TextType.IMAGE, "https://i.imgur.com/zjjcZKZ.png"),
			TextNode(", thats it.", TextType.TEXT, None)
		]
		self.assertListEqual(matches, expected)

	#
	def test_split_link(self):
		matches = split_nodes_link([TextNode("This is text with a link [to boot dev](https://www.boot.dev), thats it.", TextType.TEXT)])
		expected = [
			TextNode("This is text with a link ", TextType.TEXT, None),
			TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
			TextNode(", thats it.", TextType.TEXT, None)
		]
		self.assertListEqual(matches, expected)

	def test_split_link_single(self):
		matches = split_nodes_link([TextNode("[to boot dev](https://www.boot.dev)", TextType.TEXT)])
		expected = [
			TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
		]
		self.assertListEqual(matches, expected)

	def test_split_links(self):
		matches = split_nodes_link([TextNode("This is text with three links [to boot dev](https://www.boot.dev), [to google](https://www.google.com) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)])
		expected = [
			TextNode("This is text with three links ", TextType.TEXT, None),
			TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
			TextNode(", ", TextType.TEXT, None),
			TextNode("to google", TextType.LINK, "https://www.google.com"),
			TextNode(" and ", TextType.TEXT, None),
			TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
		]
		self.assertListEqual(matches, expected)

if __name__ == "__main__":
	unittest.main()