import tweepy


def get_tweets(username):
    consumer_key = "48ZtkwBmtGYqQPikWnbeOHSQw"
    consumer_secret = "KZ8IJQma3qJJqwrhxFLkgPW3AB6Afa5c8DYP5XiEhhvMvhg5JY"
    access_key = "1058485477727236101-MX2CtYrXn0qJR1IvJ98uPGhEh95UGp"
    access_secret = "jtxxh7ceuak2rpjcmLTPzWBv2jvZ758fQzX1sMCfXCNCf"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username, include_rts=False, tweet_mode="extended")
    tmp = []
    tweets_list = [tweet.full_text for tweet in tweets]  # CSV file created
    for j in tweets_list:
        tmp.append(j)
    new_list = list()
    new_list.append(tmp[0])
    new_list.append(tmp[1])
    return max_tweet(new_list)


def max_tweet(lista):
    maximum = 0
    max_status = ""
    for tweet in lista:
        if len(str(tweet)) > maximum:
            maximum = len(str(tweet))
            max_status = tweet
    return max_status


if __name__ == '__main__':
    name1 = input("first username: ")
    name2 = input("second username: ")
    status1 = get_tweets(name1)
    status2 = get_tweets(name2)
    if len(str(status1)) > len(str(status2)):
        print(name1)
    elif len(str(status1)) == len(str(status2)):
        print("Max tweet of both accounts has equal number of characters.")
    else:
        print(name2)

