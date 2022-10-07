from templates import article1, article2,  article3, article4, article5, article6, loops
import submitWP
import random
from primeFactorVisualizer import generateImages


n = 10365
treeImages = generateImages(n)['TreeFiles']
divisionImages = generateImages(n)['DivisionFiles']
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
formula = random.choice(posts).formula
howtocalculatelist = random.choice(posts).howtocalculatelist
factorTree = random.choice(posts).factorTree
factorTreeSteps = loops.FactorTreeMethod(n, treeImages).factorTreeSteps()
division = random.choice(posts).division
divisionSteps = loops.DivisionMethod(n, divisionImages).divisionSteps()
extra1 = random.choice(posts).extra1
faq = random.choice(posts).FAQ


# content = intro + theory + howtocalculatelist + factorTree + factorTreeSteps
content = f"{intro}{theory}{formula}{howtocalculatelist}{factorTree}{factorTreeSteps}{division}{divisionSteps}{extra1}{faq}"

print(submitWP.submit(title, content))
# print(factorTreeSteps.factorTreeSteps())
