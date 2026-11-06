from pathlib import Path
import random
i=int(input("文件数量："))
j=int(input("每个文件字符数："))
d=Path("test")
d.mkdir(exist_ok=True)
for n in range(i):
    c=''.join(chr(random.randint(0,127)) for _ in range(j))
    fp=d/f"{n}-python.txt"
    fp.write_text(c+"-python")