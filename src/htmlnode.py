class HtmlNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplemented("to_html not implemented on HtmlNode class")

	def props_to_html(self):
		if self.props is None:
			return ""
		html_props = ""
		for key, value in self.props.items():
			html_props += f' {key}="{value}"'
		return html_props

	def __repr__(self):
		return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HtmlNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("A value must be included in LeafNode class")
		if self.tag is None:
			return self.value
		if self.props is None:
			return f"<{self.tag}>{self.value}</{self.tag}>"
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" 

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HtmlNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("A tag must be included in ParentNode class")
		if self.children is None:
			raise ValueError("Children must be included in ParentNode class")
		children_html = ""
		for child in self.children: 
			children_html += child.to_html()
		return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

	def __repr__(self):
		return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

