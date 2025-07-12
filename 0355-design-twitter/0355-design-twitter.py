class Twitter:

    def __init__(self):
        self.counter=1
        self.followers={}
        self.tweets={}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId]=self.tweets.get(userId,[])+[(self.counter,tweetId)]
        self.counter+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxh=[]
        res=[]
        for c,t in self.tweets.get(userId,[]):
            heapq.heappush(maxh,(-c,t))
        if self.followers.get(userId,[]):
            for f in self.followers.get(userId,[]):
                for c,t in self.tweets.get(f,[]):
                    heapq.heappush(maxh,(-c,t))
   
        while maxh and len(res)<10:
            c,t=heapq.heappop(maxh)
            res.append(t)
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers.get(followerId,[]):
            self.followers[followerId]=self.followers.get(followerId,[])+[followeeId]
       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)