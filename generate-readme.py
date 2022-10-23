import glob
import tabulate

rows = [
	["Title", "Type", "Genre", "Files", "Source"]
]
for directory in glob.glob("data/*"):
	print(directory)
	files = len(glob.glob(f"{directory}/*.xml"))
	print(files)
	rows.append([
		"[{d}]({f})".format(d=directory.replace("data/", ""), f=directory),
		"Unkown",
		"Color    ",
		str(files),
		"[Link]()"
	])

print(
	tabulate.tabulate(rows, tablefmt="github", headers="firstrow")
)
