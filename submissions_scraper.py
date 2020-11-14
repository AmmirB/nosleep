import pandas as pd
import time
import praw
import api_tokens

start_time = time.time()

reddit = praw.Reddit (
	client_id = api_tokens.client_id,
	client_secret = api_tokens.client_secret,
	user_agent = "windows:submission_scrapper:v.1 (by /u/xanimede)"
)

ids = pd.read_csv('nosleep_top_ids.csv')

submissions = []

for index, row in ids.iterrows():
	submission = reddit.submission(id=row['id'])
	submissions.append([submission.author, submission.title, submission.created_utc, submission.num_comments, submission.score, submission.selftext, submission.id, submission.edited, submission.upvote_ratio])
	if(len(submissions) % 1000 == 0):
		submissions = pd.DataFrame(submissions, columns=['Author', 'Title', 'Date', 'Number of comments', 'Score', 'Selftext', 'ID', 'Edited', 'Upvote Ratio'])
		submissions.to_csv('nosleep_top.csv', encoding='utf-8', index=False, mode='a', header=not os.path.exists('nosleep_top.csv'))
		submissions = []


print("runtime in seconds is: %s" % (time.time() - start_time))
