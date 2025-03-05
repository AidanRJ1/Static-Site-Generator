from enum import Enum

class HtmlNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplemented()

	def props_to_html(self):
		html_props = ""
		for key, value in self.props.items():
			html_props += f' {key}="{value}"'
		
		return html_props

	def __repr__(self):
		return f"TextNode({self.tag}, {self.value}, {self.children}, {self.props})"

