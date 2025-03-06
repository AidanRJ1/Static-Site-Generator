from textnode import TextNode, TextType
from htmlnode import HtmlNode, LeafNode, ParentNode

def main():
	child_node1 = LeafNode("span", "child")
	child_node2 = LeafNode("p", "paragraph")
	parent_node = ParentNode("div", [child_node1, child_node2])
	children_html = ""

	for child in parent_node.children:
		children_html += child.to_html()3
	print(children_html)

if __name__ == "__main__":
	main()	