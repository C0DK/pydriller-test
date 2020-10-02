#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import dateutil.parser
loadjson = pd.read_json('result-1.json')
df = pd.DataFrame(loadjson)
df['date']= [dateutil.parser.parse(d).year for d in df['date']]
df.groupby(df['date']).count()['msg'].plot.bar()
plt.show()
