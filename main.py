import os, sys


def validateFile(filename: str) -> bool:
	"""
	Checks if the given file exists
	@param filename: str; defualt none
	@return: bool
	"""
	if (os.path.isfile(filename)):
		return True
	return False


def parseName(block: str) -> str:
	"""
	Takes one of the blocks and writes the name in between the two "" at the end\n
	@param block: str; defualt: none
	@return: str
	"""
	name = [char for char in block]
	name[0] = name[0].upper()

	for index, char in enumerate(name):
		if (char == "_"):
			name[index] = " "
		if (char == ":"):
			name[index:-1] = ""
	name.pop(-1)
	res: str = ""
	for char in block:
		if (char == "\""):
			res += "\""
			res += "".join(name)
			res += "\""
			break
		res += char
	res += "\n"
	return res

def main():
	if (len(sys.argv) <= 1):
		print("No file specified")

	argv = list(map(lambda x: x.lower(), sys.argv))

	try:
		filePath = argv[argv.index("-f")+1]
	except IndexError:
		print("File not found")

	if (not validateFile(filePath)):
		print("File not valid")

	r: File = open(filePath, 'r')
	lines: list[str] = [line for line in r.readlines()]
	r.close()
	startIndex: int = None
	stopIndex: list[int] = []
	count: int = 0

	for index, line in enumerate(lines):
		if (line == "####sub ideologies\n"):
			startIndex = index + 3
		if (line == "\n"): stopIndex.append(index)
	stopIndex = [i for i in stopIndex if i > startIndex]
	stopIndex = stopIndex[0]

	blocks = lines[startIndex:stopIndex]
	for index, block in enumerate(blocks):
		try:
			block.index("_desc")
			continue
		except ValueError:
			blocks[index] = parseName(block)

	lines[startIndex:stopIndex] = blocks

	w: File = open(filePath, 'w')
	w.write("".join(lines))

if __name__ == "__main__":
	main()
	sys.exit()
