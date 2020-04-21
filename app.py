punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("Input/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("Input/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

tweets = []
with open("Input/sample_twitter_data.csv", "r") as twitter_data:
    lines = twitter_data.readlines()
    #    header = lines[0]
    #    field_names = header.strip().split(',')
    for row in lines[1:]:
        tweet = row.strip().split(',')
        tweets.append(tweet)


def strip_punctuation(word):
    word = [char for char in word if char not in punctuation_chars]
    word = ''.join(word)
    return word


def get_scores(data):
    data = data.split()
    positive_score = len([w.lower() for w in data if w in positive_words])
    negative_score = len([w.lower() for w in data if w in negative_words])
    net_score = positive_score - negative_score
    sentiment = positive_score, negative_score, net_score
    sentiment = list(sentiment)
    return sentiment


with open("Output/resulting_data.csv", "w") as results:
    results.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    results.write('\n')
    for tweet in tweets:
        result = get_scores(strip_punctuation(tweet[0]))
        row_string = '{},{},{},{},{}'.format(tweet[1], tweet[2], result[0], result[1], result[2])
        results.write(row_string + '\n')
