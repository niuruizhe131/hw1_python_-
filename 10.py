from pathlib import Path
import random
d=Path("img")
ps=list(d.glob("*.png"))
for f in random.sample(ps,50): 
    f.rename(f.with_suffix(".jpg"))