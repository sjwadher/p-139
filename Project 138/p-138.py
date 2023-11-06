import pandas as pd

df1 = pd.read_csv("shared_articles.csv")

df2 = pd.read_csv("users_interactions.csv")


print(df1.head(5))

print(df2.head(5))


# ---------------------------------- project 139 ---------------------------------------------------

print(df1[['title', 'eventType']].head(10))

df1 = df1[df1['eventType'] == 'CONTENT SHARED']

print(df1.head())

def find_total_events(df1_row):
  total_likes = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "LIKE")].shape[0]
  total_views = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "VIEW")].shape[0]
  total_bookmarks = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "BOOKMARK")].shape[0]
  total_follows = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "FOLLOW")].shape[0]
  total_comments = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "COMMENT CREATED")].shape[0]
  
  return total_likes + total_views + total_bookmarks + total_follows + total_comments

df1["total_events"] = df1.apply(find_total_events, axis=1)

df1 = df1.sort_values(['total_events'], ascending=[False])

print(df1[['title', 'eventType']].head(10))


 