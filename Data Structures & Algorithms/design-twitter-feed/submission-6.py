class Twitter:  
    def __init__(self):
        self.timer = 0 # time cntr for tweets
        self.followMap = {} # userId -> set(followeeId)
        self.tweetMap = {} # userId -> sort list of tweets (by time of posting)

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
            self.followMap[userId] = set()
        self.tweetMap[userId].append((self.timer, tweetId))
        self.timer -= 1

        
    def getNewsFeed(self, userId: int) -> List[int]:
        tempFeed = []
        ids = set([userId] + list(self.followMap[userId]))
        for user in ids:
            n, cnt = len(self.tweetMap[user]), 10
            i = n - 1
            while (i >= 0) and (cnt >= 0):
                heapq.heappush(tempFeed, self.tweetMap[user][i])
                i -= 1
                cnt -= 1
        n, cnt = len(tempFeed), 10
        newsFeed = []
        while n > 0 and cnt > 0:
            time, tweet = heapq.heappop(tempFeed)
            newsFeed.append(tweet)
            n -= 1
            cnt -= 1
        return newsFeed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
            self.tweetMap[followerId] = []
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            return
        if followeeId not in self.followMap[followerId]:
            return
        self.followMap[followerId].remove(followeeId)
            
