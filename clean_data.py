import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

columns = ['letter', 'xbox', 'ybox', 'width', 'high', 'onpix', 'xbar',
           'ybar', 'x2bar', 'y2bar', 'xybar', 'x2ybr', 'xy2br',
           'xedge', 'xedgey', 'yedge', 'yedgex']

df = pd.read_csv("letters.csv", names=columns)

df.columns = df.columns.str.strip()

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.dropna(inplace=True)

scaler = StandardScaler()
df[df.columns[1:]] = scaler.fit_transform(df[df.columns[1:]])

print(df.info())
print(df.head())

sns.countplot(x='letter', data=df)
plt.title("Letter Distribution")
plt.show()
