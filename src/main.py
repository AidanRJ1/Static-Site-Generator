from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import split_nodes_image, split_nodes_link, extract_markdown_links, text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
import os, shutil

def copy_to_directory(src, dst):
	if os.path.exists(dst):
		print(f"deleting '{dst}'")
		shutil.rmtree(dst)

	print(f"making '{dst}'")
	os.mkdir(dst)
	src_contents = os.listdir(src)
	for file in src_contents:
		if os.path.isfile(f"{src}/{file}"):
			print(f"copying '{src}/{file}' to '{dst}'")
			shutil.copy(f"{src}/{file}", dst)
			continue
		else:
			print(f"'{src}/{file}' is a directory")
			copy_to_directory(f"{src}/{file}", f"{dst}/{file}")
	return
	

def main():
	copy_to_directory("./static", "./public")

if __name__ == "__main__":
	main()	