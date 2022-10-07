from templates import article1, article2,  article3, article4, article5, article6, loops
import submitWP
import random
from primeFactorVisualizer import generateImages
from datetime import timedelta, datetime


# n = 10365
current_time = datetime.now()
numbers = [320, 10365, 46, 54, 69, 104, 326]

for i in range(0, len(numbers)):
    n = numbers[i]
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
    factorTreeSteps = loops.FactorTreeMethod(
        n, numbers, i, treeImages).factorTreeSteps()
    division = random.choice(posts).division
    divisionSteps = loops.DivisionMethod(
        n, numbers, i, divisionImages).divisionSteps()
    extra1 = random.choice(posts).extra1
    faq = random.choice(posts).FAQ

    # content = intro + theory + howtocalculatelist + factorTree + factorTreeSteps
    content = f"{intro}{theory}{formula}{howtocalculatelist}{factorTree}{factorTreeSteps}{division}{divisionSteps}{extra1}{faq}"

    tdelta = timedelta(minutes=random.randrange(3, 7))
    current_time = current_time + tdelta
    time = schedule(current_time)

    WPrequest = submitWP.submit(title, content, time)
    print(f"Number - {i+1} is scheduled at {time} with {WPrequest.text}")
    # print(factorTreeSteps.factorTreeSteps())
