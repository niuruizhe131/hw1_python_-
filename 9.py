from pathlib import Path
import random,string
d=Path("img")
d.mkdir(exist_ok=True)
for _ in range(100):
    n=''.join(random.choices(string.ascii_uppercase+"0123456789",k=4))
    (d/f"{n}.png").touch()