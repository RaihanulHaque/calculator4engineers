from templates import article1, article2,  article3, article4, article5, article6, loops
import submitWP
import random
from primeFactorVisualizer import generateImages
from datetime import timedelta, datetime


def schedule(current_time):
    # tdelta = timedelta(minutes=random.randrange(3, 9))
    # current_time = current_time + tdelta
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    second = str(current_time.second)
    if len(hour) == 1:
        hour = f"0{hour}"
    if len(minute) == 1:
        minute = f"0{minute}"
    if len(second) == 1:
        second = f"0{second}"
    return f"{current_time.date()}T{hour}:{minute}:{second}"


# n = 10361
current_time = datetime.now()
# numbers = [601, 604, 613, 10365, 631, 632, 633, 634]
numbers = [2**8, 2**9, 2**10]

for i in range(0, len(numbers)):
    n = numbers[i]
    treeImages = generateImages(n)['TreeFiles']
    divisionImages = generateImages(n)['DivisionFiles']
    bannerImages = generateImages(n)['Banners']
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
    extra2 = random.choice(posts).extra2
    faq = random.choice(posts).FAQ

    # content = intro + theory + howtocalculatelist + factorTree + factorTreeSteps
    content = f"{intro}{theory}{formula}{howtocalculatelist}{factorTree}{factorTreeSteps}{division}{divisionSteps}{extra1}{extra2}{faq}"

    tdelta = timedelta(minutes=random.randrange(1, 3))
    current_time = current_time + tdelta
    time = schedule(current_time)

    WPrequest = submitWP.submit(title, n, content, time, bannerImages)
    print(f"Number - {i+1} is scheduled at {time} with {WPrequest}")
