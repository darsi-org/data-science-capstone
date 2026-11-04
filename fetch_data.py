"""Download the UCI Student Performance data (Portuguese course, 649 students) into data/students.csv."""
import pathlib

from ucimlrepo import fetch_ucirepo

ds = fetch_ucirepo(id=320)
df = ds.data.features.join(ds.data.targets)
pathlib.Path("data").mkdir(exist_ok=True)
df.to_csv("data/students.csv", index=False)
print(df.shape, "saved to data/students.csv")
