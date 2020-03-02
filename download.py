import tweepy  # https://github.com/tweepy/tweepy
import csv
import json

# Twitter API credentials
consumer_key = "XXXXX"
consumer_secret = "XXXXX"
access_key = "XXXXXX"
access_secret = "XXXXXX"


def get_all_tweets(screen_name):
	# Twitter only allows access to a users most recent 3240 tweets with this method

	# authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	# initialize a list to hold all the tweepy Tweets
	alltweets = []

	# make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(
			screen_name=screen_name, count=200, include_rts=False, tweet_mode="extended", trim_user=True)

	# save most recent tweets
	alltweets.extend(new_tweets)

	# save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	# keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before " + str(oldest))

		# all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(
			screen_name=screen_name, count=200, max_id=oldest)

		# save most recent tweets
		alltweets.extend(new_tweets)

		# update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print("tweets downloaded so far: " + str(len(alltweets)))

	with open('raw_data.json', 'w', encoding='utf-8') as f:
		json.dump([status._json for status in alltweets],
							f, ensure_ascii=False, indent=4)

	# pass


if __name__ == '__main__':
	# pass in the username of the account you want to download
	get_all_tweets("realDonaldTrump")
