from textnode import TextNode, TextType
from htmlnode import HtmlNode
from leafnode import LeafNode

def main():
	node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com", "target": "_blank"})
	print(node.props)

if __name__ == "__main__":
	main()	