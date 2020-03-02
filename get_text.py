
import json
import re

with open('tweet_history.json', 'r') as f:
    tweets = json.load(f)


text_tweets_ary_1 = [re.sub(r"http\S+", "", x['text']) for x in tweets]
text_tweets_ary = [re.sub('RT @[\w_]+: ', '', x) for x in text_tweets_ary_1]
text_tweets = "\n".join([x.rstrip() for x in text_tweets_ary if x.strip() and len(x) > 10]).replace("\n\n", "\n")

with open('text.txt', 'w', encoding='utf-8') as f:
		# json.dump(text_tweets,
		# 					f, ensure_ascii=False, indent=4)
        f.write(text_tweets)
