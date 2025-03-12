from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode, LeafNode 
from inline_markdown import text_to_textnodes
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

def heading_to_html_node(heading):
	count = 0
	for char in heading:
		if char == "#":
			count += 1
		else:
			break
	return LeafNode(f"h{count}", heading[count + 1:])

def code_block_to_html_node(code_block):
	#html_node = LeafNode("code", repr(code_block.strip("```").lstrip("\n")).strip("'"))
	#return ParentNode("pre", [html_node])
	text = code_block.strip("```").lstrip("\n")
	raw_text_node = TextNode(text, TextType.TEXT)
	child = text_node_to_html_node(raw_text_node)
	code = ParentNode("code", [child])
	return ParentNode("pre", [code])

def quote_block_to_html_node(quote_block):
	new_block = []
	for line in quote_block:
		new_block.append(line.lstrip(">").replace("\n", ""))
	content = "".join(new_block)
	return LeafNode("blockquote", content.strip())

def unordered_list_to_html_node(ordered_list):
	html_nodes = []
	lines = ordered_list.split("\n")
	for line in lines:
		html_nodes.append(ParentNode("li", text_to_html_nodes(line.lstrip("- "))))
	return ParentNode("ul", html_nodes)

def ordered_list_to_html_node(ordered_list):
	html_nodes = []
	lines = ordered_list.split("\n")
	for i in range(len(lines)):
		html_nodes.append(ParentNode("li", text_to_html_nodes(lines[i].lstrip(f"{i + 1}. "))))
	return ParentNode("ol", html_nodes)

def text_to_html_nodes(text):
	html_nodes = []
	text_nodes = text_to_textnodes(text)
	for node in text_nodes:
		html_nodes.append(text_node_to_html_node(node))
	return html_nodes

def block_to_html_node(block):
	node_type = block_to_block_type(block.strip())
	match(node_type):
		case BlockType.PARAGRAPH:
			return ParentNode("p", text_to_html_nodes(block.strip().replace("\n", " ")))	
		case BlockType.HEADING:
			return heading_to_html_node(block)
		case BlockType.CODE:
			return code_block_to_html_node(block)
		case BlockType.QUOTE:
			return quote_block_to_html_node(block)
		case BlockType.UNORDERED_LIST:
			return unordered_list_to_html_node(block)
		case BlockType.ORDERED_LIST:
			return ordered_list_to_html_node(block)
		case _:
			raise ValueError(f"invalid node type: {node_type}")

def markdown_to_html_node(markdown):
	html_nodes = []
	markdown_blocks = markdown_to_blocks(markdown)
	for block in markdown_blocks:
		html_nodes.append(block_to_html_node(block))
	return ParentNode("div", html_nodes)