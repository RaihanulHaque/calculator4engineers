from templates import article1, article2,  article3, article4, article5, article6, loops
import submitWP
import random
from primeFactorVisualizer import generateImages


n = 10365
treeImages = generateImages(n)['TreeFiles']
p1 = article1.Post(n)
p2 = article2.Post(n)
p3 = article3.Post(n)
p4 = article4.Post(n)
p5 = article5.Post(n)
p6 = article6.Post(n)
posts = [p1, p2, p3, p4, p5, p6]

title = random.choice(posts).title
intro = random.choice(posts).intro
theory = random.choice(posts).theory
howtocalculatelist = random.choice(posts).howtocalculatelist
factorTree = random.choice(posts).factorTree
factorTreeSteps = loops.Ftree(n, treeImages)


# content = intro + theory + howtocalculatelist + factorTree + factorTreeSteps
# content = f"{intro}{theory}{howtocalculatelist}{factorTree}{factorTreeSteps}"

# print(submitWP.submit(title, content))
print(factorTreeSteps)
