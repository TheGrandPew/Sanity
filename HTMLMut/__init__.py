import random
import HTMLMut.settings

def blackstrip(tags):
	for name in tags:
		if settings.blacklist.get(name):
			btgs = settings.blacklist[name]
			for btg in btgs:
				try:
					idx = tags[name].index(btg)
					tags[name].pop(idx)
				except Exception as e:
					print(e)
		else:
			pass
	return tags

class HtmlBuilder:
	def __init__(self):
		settings.htags = blackstrip(settings.htags)
		#settings.htags['double'].extend(settings.stags['double'])
		#settings.htags['double'].extend(settings.mtags['double'])
	def generate(self):
		self.building = f"{self.genBlock()}{self.genBlock()}{self.genBlock()}"
		return self.building

	def genBlock(self):
		return random.choice([TSingle().gen(),TDouble().gen(),TDouble().gen(),TDouble().gen(),TBoth().gen(),TTable().gen()])

class TSingle:
	def __init__(self):
		self.tags = settings.htags['single']

	def gen(self):
		return f"<{random.choice(self.tags)}>"

class TDouble:
	def __init__(self):
		self.tags = settings.htags['double']

	def gen(self):
		parent = random.choice(self.tags)
		choices = [self.genSimp(),self.genSimp(),self.genSimp()]
		choices.append(f"<{parent}>{self.genChildren()}</{parent}>")
		choices.append(f"<{parent}>{self.genChildren()}")
		choices.append(f"<{parent}>{self.genChildren()}</{parent}>")
		return random.choice(choices)
	def genChildren(self):
		parent = random.choice(self.tags)
		out = f"<{parent}>"
		for i in range(random.randint(0,settings.deepness)):
			out += self.genChild()
		out += f"</{parent}>"
		return out

	def genChild(self):
		parent = random.choice(self.tags)
		choices = [self.genSimp(),self.genSimp(),self.genSimp(),f"<{parent}>{self.genSimp()}</{parent}>"]
		return random.choice(choices)

	def genSimp(self):
		parent = random.choice(self.tags)
		choices = []
		choices.append(f"<{parent}>{random.choice(settings.fillers)}</{parent}>")
		choices.append(f"<{parent}>{random.choice([TSingle().gen()])}</{parent}>")
		return random.choice(choices)
class TBoth:
	def __init__(self):
		self.tags = settings.htags['both']

	def gen(self):
		choices = [f"<{random.choice(self.tags)}>",f"</{random.choice(self.tags)}>",f"<{random.choice(self.tags)}>{random.choice([TSingle().gen(),TDouble().gen(),TText().gen()])}"]
		return random.choice(choices)

class TTable:
	def __init__(self):
		self.tags = settings.htags['special']['table']

	def gen(self):
		out = "<table>"
		out += self.genInnerTable()
		out += "</table>"
		return out

	def genInnerTable(self):
		choices = []
		choices.append(f"<td>{random.choice([TSingle().gen(),TDouble().gen(),TBoth().gen(),TText().gen()])}</td>")
		choices.append(f"<{random.choice(self.tags)}>")
		choices.append(f"<{random.choice(self.tags)}><{random.choice(self.tags)}>")
		choices.append(f"<{random.choice(self.tags)}><{random.choice(self.tags)}></tbody><{random.choice(self.tags)}>")
		return random.choice(choices)

class TText:
	def __init__(self):
		self.tags = settings.htags['special']['text']

	def gen(self):
		choices = []
		p1 = random.choice(self.tags)
		choices.append(f"<{p1}>h1{'{'} {random.choice(settings.fillers)}</{p1}>")
		choices.append(f"<{p1}>{TSingle().gen()}</{p1}>")
		choices.append(f"<{p1}><{p1}>XXD</{p1}>DD</{p1}>")
		return random.choice(choices)
