from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for old_node in old_nodes:
		old_text = old_node.text
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		split_nodes = []
		split_text = old_text.split(delimiter)
		if len(split_text) % 2 == 0:
			raise ValueError("invalid markdown, formatted section not closed")
		for i in range(len(split_text)):
			if split_text[i] == "":
				continue
			if i % 2 == 0:
				split_nodes.append(TextNode(split_text[i], TextType.TEXT))
			else:
				split_nodes.append(TextNode(split_text[i], text_type))
		new_nodes.extend(split_nodes)
	return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		old_text = old_node.text
		images = extract_markdown_images(old_text)
		if len(images) == 0:
			new_nodes.append(old_node)
			continue
		for image in images:
			(image_alt, image_link) = image
			split_text = old_text.split(f"![{image_alt}]({image_link})", 1)
			if len(split_text) != 2:
				raise ValueError("invalid markdown, formatted section not closed")
			if split_text[0] != "":
				new_nodes.append(TextNode(split_text[0], TextType.TEXT))
			new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
			old_text = split_text[1]
		if old_text != "":
			new_nodes.append(TextNode(old_text, TextType.TEXT))
	return new_nodes

def split_nodes_link(old_nodes):
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		old_text = old_node.text
		links = extract_markdown_links(old_text)
		if len(links) == 0:
			new_nodes.append(old_node)
			continue
		for link in links:
			(link_text, link_url) = link
			split_text = old_text.split(f"[{link[0]}]({link[1]})", 1)
			if len(split_text) != 2:
				raise ValueError("invalid markdown, formatted section not closed")
			if split_text[0] != "":
				new_nodes.append(TextNode(split_text[0], TextType.TEXT))
			new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
			old_text = split_text[1]
		if old_text != "":
			new_nodes.append(TextNode(old_text, TextType.TEXT))
	return new_nodes

def text_to_textnodes(text):
	nodes = [TextNode(text, TextType.TEXT)]
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
	nodes = split_nodes_image(nodes)
	nodes = split_nodes_link(nodes)
	return nodes