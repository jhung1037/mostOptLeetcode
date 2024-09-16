class Tweet:
    def __init__(self, userID, tweetId, next=None):
        self.userID = userID
        self.tweetId = tweetId
        self.next = next

class Twitter:

    def __init__(self):
        self.users = {} # record user and its followee {int:set}
        self.dummy_tweet = Tweet(-1,-1)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {userId}
        tweet = Tweet(userId, tweetId, self.dummy_tweet.next)
        self.dummy_tweet.next = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = []
        feed = self.dummy_tweet.next
        while feed and len(feeds) < 10:
            if feed.userID in self.users[userId]:
                feeds.append(feed.tweetId)
            feed = feed.next
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = {followerId}
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)