from textnode import TextNode, TextType
from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import split_nodes_image, split_nodes_link, extract_markdown_links, text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type

def main():
	block = """
- Item
- Item 2
- Item 3
"""
	block_to_block_type(block.strip())


if __name__ == "__main__":
	main()	