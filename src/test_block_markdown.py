import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

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

if __name__ == "__main__":
	unittest.main()