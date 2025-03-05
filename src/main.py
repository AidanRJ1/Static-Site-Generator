from textnode import TextNode, TextType
from htmlnode import HtmlNode

def main():
	test = HtmlNode("a", "This is text", ["node", "node1"], {"href": "https://www.google.com", "target": "_blank"})
	print(test.props_to_html())

if __name__ == "__main__":
	main()	