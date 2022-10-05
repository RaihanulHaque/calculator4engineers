from templates import post1
from templates import article2
import random

n = 44
p1 = post1.Post(n)
p2 = article2.Post(n)
posts = [p1, p2]

title = random.choice(posts).title
intro = random.choice(posts).intro

print(f"title:\n {title}")
print()
print(f"intro:\n{intro}")
