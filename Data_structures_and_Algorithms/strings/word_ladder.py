# just checking all the possibilites and adding in set to make sure not visited again
# plain greedy approach
from collections import deque
def word_ladder(beginWord, endWord, wordList):

    def construct(word_List):
        d={}
        for word in word_List:
            for i in range(len(word)):
                s=word[:i]+"_"+word[i+1:]
                d[s] = d.get(s,[])+[word]
        return d

    def bfs(begin, end, dict_words):
        queue, visited = deque([(begin,1)]), set()
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)

                if word==end:
                    return steps

                for i in range(len(word)):
                    s=word[:i]+"_"+word[i+1:]
                    neighbours = dict_words.get(s,[])
                    for n in neighbours:
                        if n not in visited:
                            queue.append((n,steps+1))
        return 0


    d = construct(wordList|set([beginWord])) # we might not need the end word as it might not exist in the dictionary provided to make a path
    return bfs(beginWord, endWord, d)

print(word_ladder('','', ["hot","dot","dog","lot","log","cog"]))


































    # queue = [(beginWord,1)]
    # visited = set()
    #
    # while queue:
    #     word,dist = queue.pop(0)
    #     if word == endWord:
    #         return dist
    #
    #     for  i in range(len(word)):
    #         for j in 'abcdefghijklmnopqrstuvwxyz':
    #             temp = word[:i]+j+word[i+1:]
    #             if temp not in visited and temp in wordList:
    #                 queue.append((temp,dist+1))
    #                 visited.add(temp)
    #
    #     return 0