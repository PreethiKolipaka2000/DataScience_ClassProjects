import pandas as pd 
def make1_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">{text}</a>'

def make_clickable(val):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)

df=pd.read_csv("zomato.csv")
df.style.format({'url': make_clickable})
df1=df[['url','name']]
df1.to_html('details1.html')
