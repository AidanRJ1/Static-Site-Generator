import unittest
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
	def test_markdown_to_blocks(self):
	    markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
	    matches = markdown_to_blocks(markdown)
	    expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
	    self.assertEqual(matches, expected)

    #
	def test_block_to_block_type_paragraph(self):
		block = """
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.PARAGRAPH
		self.assertEqual(matches, expected)

	def test_block_to_block_type_heading(self):
		block = """
# Heading
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.HEADING
		self.assertEqual(matches, expected)

	def test_block_to_block_type_code(self):
		block = """
```This is a code block```
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.CODE
		self.assertEqual(matches, expected)

	def test_block_to_block_type_quote(self):
		block = """
>This
>Is
>a
>quote block
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.QUOTE
		self.assertEqual(matches, expected)

	def test_block_to_block_type_quote(self):
		block = """
>This
Is
>a
>quote block
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.PARAGRAPH
		self.assertEqual(matches, expected)

	def test_block_to_block_type_unordered_list(self):
		block = """
- Item
- Item 2
- Item 3
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.UNORDERED_LIST
		self.assertEqual(matches, expected)

	def test_block_to_block_type_error_unordered_list(self):
		block = """
- Item
 Item 2
- Item 3
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.PARAGRAPH
		self.assertEqual(matches, expected)

	def test_block_to_block_type_ordered_list(self):
		block = """
1. Item
2. Item
3. Item
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.ORDERED_LIST
		self.assertEqual(matches, expected)

	def test_block_to_block_type_error_ordered_list(self):
		block = """
1. Item
3. Item
4. Item
"""
		matches = block_to_block_type(block.strip())
		expected = BlockType.PARAGRAPH
		self.assertEqual(matches, expected)

	#
	def test_markdown_to_html_node_paragraph(self):
		markdown = """
This is **bolded** paragraph
text in a p
tag here
"""
		html_node = markdown_to_html_node(markdown)
		matches = html_node.to_html()
		expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>"
		self.assertEqual(matches, expected)

	def test_markdown_to_html_node_paragraphs(self):
		markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
		html_node = markdown_to_html_node(markdown)
		matches = html_node.to_html()
		expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
		self.assertEqual(matches, expected)

	def test_markdown_to_html_node_heading(self):
		markdown = """
# This is a heading
"""
		html_node = markdown_to_html_node(markdown)
		matches = html_node.to_html()
		expected = "<div><h1>This is a heading</h1></div>"
		self.assertEqual(matches, expected)

	def test_markdown_to_html_node_headings(self):
		markdown = """
# This is a heading

### This is a subheading

Plus some text
"""
		html_node = markdown_to_html_node(markdown)
		matches = html_node.to_html()
		expected = "<div><h1>This is a heading</h1><h3>This is a subheading</h3><p>Plus some text</p></div>"
		self.assertEqual(matches, expected)

	def test_markdown_to_html_node_code(self):
		markdown = """
```
This is a `code` block
With some _italic_ text
```
"""
		html_node = markdown_to_html_node(markdown)
		matches = html_node.to_html()
		expected = r"<div><pre><code>This is a `code` block\nWith some _italic_ text\n</code></pre></div>"
		self.assertEqual(matches, expected)

	def test_markdown_to_html_node_quote(self):
		markdown = """
> This is a
> blockquote block

this is paragraph text

"""
		html_node = markdown_to_html_node(markdown)
		matches = html_node.to_html()
		expected = "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"
		self.assertEqual(matches, expected)

	def test_markdown_to_html_node_lists(self):
		markdown = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""
		html_node = markdown_to_html_node(markdown)
		matches = html_node.to_html()
		expected = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
		self.assertEqual(matches, expected)




if __name__ == "__main__":
	unittest.main()