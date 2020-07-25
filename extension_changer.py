from os import listdir, system
from os.path import isfile, join

from_ext, to_ext = input().split()
files = [f for f in listdir("./") if (isfile(join("./", f))) and f.endswith(f".{from_ext}")]
converted = 0
total = len(files)

for name in files:
	if name.endswith(f".{from_ext}"):
		name = name[:len(name)-4]
		system(f"mv {name}.{from_ext} {name}.{to_ext}")
		converted += 1
		print(f"file {name} has been converted\n({converted}/{total})")
