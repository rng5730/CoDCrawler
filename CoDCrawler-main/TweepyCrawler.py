import tweepy
import json
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("JPTDYUTk5FFA22yDXUwWqNA4F", "r8ySz1orfQTNNmT3TP7UULxuRTF4KMWHFKXqYZ7XXxD2077H3F")
auth.set_access_token("1420930922401042433-OiqKEN7MPbagVBVTb8bREvFCEesq3Y", "4Cm7LikMZ502ZBrCQvrPDAjz42ioFCfTpwXm8uLH"
                                                                            "LsiOD")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

def scrape(keywords, limit):
    program_start = time.time()
    for i in range(0, 1):
        start_run = time.time()
        with open('data/tweepy ' + keywords + '.txt', 'w', encoding='utf-8') as f:
            tweets = tweepy.Cursor(api.search, q=keywords, lang="en", result_type="recent", tweet_mode='extended').\
                items(limit)
            tweet_list = [tweet for tweet in tweets]
            noTweets = 0
            for tweet in tweet_list:
                name = tweet.user.name
                username = tweet.user.screen_name
                tweetcreatedts = tweet.created_at
                retweetcount = tweet.retweet_count
                hashtags = tweet.entities['hashtags']
                try:
                    text = tweet.retweeted_status.full_text
                except AttributeError:  # Not a Retweet
                    text = tweet.full_text
                noTweets += 1
                reviewDict = {
                    'Tweet#': noTweets,
                    'TweetCreatedDate': str(tweetcreatedts),
                    'RetweetCount': retweetcount,
                    "Name": name,
                    'Username': username,
                    'Text': text,
                    'Hashtags': hashtags
                }
                f.write(json.dumps(reviewDict)+'\n')
            end_run = time.time()
            duration_run = round((end_run - start_run) / 60, 2)

            print('no. of tweets scraped for run {} is {}'.format(i + 1, noTweets))
            print('time take for {} run to complete is {} mins'.format(i + 1, duration_run))
            f.flush()
        program_end = time.time()
        print('Scraping has completed')
        print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start) / 60, 2))


if __name__ == "__main__":
    scrape("#whomademyclothes", limit=1000)
