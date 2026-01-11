class User:
    def __init__(self):
        self.following = set()
        self.followers = set()
        self.posts = []


class Twitter:
    def __init__(self):
        self.users = defaultdict(User)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].posts.append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        NUM = 10

        user = self.users[userId]

        recent_posts = NUM
        i = len(user.posts) - 1
        while i >= 0 and recent_posts > 0:
            heapq.heappush(heap, user.posts[i])
            recent_posts -= 1
            i -= 1

        for fid in user.following:
            friend = self.users[fid]
            num_posts = NUM
            i = len(friend.posts) - 1

            while i >= 0 and num_posts > 0:
                heapq.heappush(heap, friend.posts[i])
                num_posts -= 1
                i -= 1

        for _ in range(min(NUM, len(heap))):
            res.append(heapq.heappop(heap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].following.add(followeeId)
        self.users[followeeId].followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].following.discard(followeeId)
        self.users[followeeId].followers.discard(followerId)
