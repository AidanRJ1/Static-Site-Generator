from textnode import TextNode, TextType
from enum import Enum
import re

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered list"
	ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
	markdown_blocks = markdown.strip("\n").strip().split("\n\n")
	return markdown_blocks

def block_to_block_type(markdown_block):
	block_lines = markdown_block.split("\n")
	if re.search("^#{1,6} ", markdown_block):
		return BlockType.HEADING
	elif re.search("^```", markdown_block) and re.search("```$", markdown_block):
		return BlockType.CODE
	elif re.search("^>", markdown_block):
		for block_line in block_lines:
			if re.search("^>", block_line.lstrip()):
				continue
			else:
				return BlockType.PARAGRAPH
		return BlockType.QUOTE
	elif re.search("^- ", markdown_block):
		for block_line in block_lines:
			if re.search("^- ", block_line.lstrip()):
				continue
			else:
				return BlockType.PARAGRAPH
		return BlockType.UNORDERED_LIST
	elif re.search("^[1234567890]. ", markdown_block):
		count = 1
		for block_line in block_lines:
			if re.search("^[1234567890]. ", block_line.lstrip()) and block_line[0] == f"{count}":
				count += 1
				continue
			else:
				return BlockType.PARAGRAPH
		return BlockType.ORDERED_LIST
	else:
		return BlockType.PARAGRAPH