import numpy as np
import pandas as pd

df.read_csv('articles')

df = df.sort_values(['total_events'], ascending=[False])

output = df[["url", "text", "lang","total_events"]].head(20).value.tolist()


