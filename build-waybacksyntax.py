import pandas as pd

csv = pd.read_csv('./vid-url-timestamp.csv', sep=',', index_col=False,
quotechar='"', names=["indexlucene", "url", "timestamp"])

for index, row in csv.iterrows():
    timestamp = row['timestamp']
    # convert to wayback syntax
    timestamp = timestamp.replace('-', '')
    timestamp = timestamp.replace(' ', '')
    timestamp = timestamp.replace(':', '')
    print timestamp + '/' + row['url']
