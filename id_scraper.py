from psaw import PushshiftAPI
import praw
import time
import pandas as pd
import api_tokens

start_time = time.time()

reddit = praw.Reddit (
	client_id = api_tokens.client_id,
	client_secret = api_tokens.client_secret,
	user_agent = "windows:submission_scrapper:v.1 (by /u/xanimede)"
)

api = PushshiftAPI(reddit)


gen = api.search_submissions(subreddit='nosleep', filter='id')

submissions = []

for submission in gen:
	submissions.append(submission)

submissions_df = pd.DataFrame(submissions, columns=['id'])


submissions_df.to_csv('nosleep_top_ids.csv', encoding='utf-8', index=False)

print("runtime in seconds is: %s" % (time.time() - start_time))
