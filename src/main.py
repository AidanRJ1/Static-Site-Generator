from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import split_nodes_image, split_nodes_link, extract_markdown_links, text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
import os, shutil, sys

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

def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line.strip("# ")
		else:
			raise Exception("No h1 header exists")

def generate_page(from_path, template_path, dest_path, BASEPATH):
	directories = os.path.dirname(dest_path)
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	print(f"Reading '{from_path}'")
	with open(from_path, "r") as file:
		markdown = file.read()
	print(f"Extracting title from '{from_path}")
	title = extract_title(markdown)
	print("Converting markdown to html")
	html_node = markdown_to_html_node(markdown)
	html = html_node.to_html()
	print(f"Reading '{template_path}'")
	with open(template_path, "r") as file:
		template = file.read()
	edited_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html).replace('href="/', f'href="{BASEPATH}').replace('src="/', f'src="{BASEPATH}')
	if not os.path.exists(directories):
		print(f"Making {directories}")
		os.makedirs(directories)
	print(f"Writing edited template to '{dest_path}'")
	with open(dest_path, "w") as file:
		file.write(edited_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, BASEPATH):
	src_contents = os.listdir(dir_path_content)
	for file in src_contents:
		if os.path.isfile(f"{dir_path_content}/{file}"):
			generate_page(f"{dir_path_content}/{file}", template_path, f"{dest_dir_path}/index.html", BASEPATH)
			#print(f"Is File - Src: {dir_path_content}/{file} Dst: {dest_dir_path}/index.html")
			continue
		else:
			#print(f"Is Directory - Src: {dir_path_content}/{file} Dst:{dest_dir_path}/{file}")
			generate_pages_recursive(f"{dir_path_content}/{file}", template_path, f"{dest_dir_path}/{file}", BASEPATH)
			
	return

def main():
	if sys.argv[1]:
		BASEPATH = sys.argv[1]
	else:
		BASEPATH = "/"
	copy_to_directory("./static", "./public")
	#generate_page("content/index.md", "template.html", "public/index.html")
	generate_pages_recursive("./content", "./template.html", "./public", BASEPATH)

if __name__ == "__main__":
	main()	