#!/usr/bin/env python
# coding: utf-8

# In[6]:


import collections


# In[7]:


def bfs(graph, root):
    seen, queue = set([root]), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


# In[10]:


def bfs1(graph, root,a):
    seen, queue = set([root]), collections.deque([root])
    temp=0
    while queue:
        vertex = queue.popleft()
        if(vertex==a):
            temp=1
            print(a,"is in the list")
            break
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    if(temp==0):
          print(a, "  is not in the list")


# In[11]:


def visit(n):
    print(n)


# In[13]:


if __name__ == '__main__':
    graph = {1: [48308, 48311],
             48308: [6996],
             48311:[7005,51646],
             6996: [16043],
             7005: [6996],
             51646: [51640],
             16043:[9987,71840],
             9987: [8150],
             51640:[51641],
             71840: [8150],
             51641:[51179],
             51179:[8150],
             2: [7005],
             3: [8150],
             8150: []
             }
    print("\nplease enter the node from where you want to start traversing:")
    b=int(input())
    bfs(graph,b)
    print("\nplease enter the node you want to search:")
    a=int(input())
    bfs1(graph,1, a)


# In[ ]:




