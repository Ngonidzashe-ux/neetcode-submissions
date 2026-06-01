"""
Understand:
1. Track the posts by a user. hashmap storing userid and a list of tweets
2. Track the followers of a user. hashmap storing userid and followers
3. The idea of using a graph just came to me. Directed graph that points to who one is following. maybe too commplex
4.getnews feed: track the time of posting, create a max heap.
5. I am thinking if we should have a maxheap of each user that is capped at 10, that is better
Match:
Plan:
__init__
self.posts = collections.defaultdict(list)
self.followers = collections.defaultdict(list)
self.newsfeed = collections.defaultdict(list)
self.time = 0

postTweet:
-increment the time
- add the tweetid in the userid list
- add (time, tweetid, userid) to the userid's heap
- for all people that follow the user.id, this should be put in their heaps too while mantaining the 10 value

getNewsfeed:
return a list of everything in the heap

follow:
add the follower id to the list of the followee

unfollow:
remove the follower id from the list of the followe
"""

class Twitter:

    def __init__(self):
        self.posts = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.posts[userId].append((self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        heap = []
        res = []
        for followeeId in self.following[userId]:
            if followeeId in self.posts:
                index = len(self.posts[followeeId]) - 1
                time, tweetId = self.posts[followeeId][index]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])

        while heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.posts[followeeId][index]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])
        return res




        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

