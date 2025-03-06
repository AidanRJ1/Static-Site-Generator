from htmlnode import HtmlNode

class LeafNode(HtmlNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)
			

	def to_html(self):
		if self.value == None:
			raise ValueError()

		if self.tag == None:
			return self.value

		if self.props == None:
			return f"<{self.tag}>{self.value}</{self.tag}>"

		# super().props_to_html() returning None Value
		return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>" 