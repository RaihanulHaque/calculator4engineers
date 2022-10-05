import random
from math import floor, sqrt
import submitWP
import requests
import base64
import json


class FactorTree:
    def __init__(self, n, treeImages):
        self.n = n
        # self.index = index
        self.treeImages = treeImages
        self.content = self.factorTreeSteps()

    def authenticate(self):
        user = "Rahi"
        password = "t5nC 34nz obVc BUzM c1Nt KQnK"
        creds = user + ':' + password
        cred_token = base64.b64encode(creds.encode())
        header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
        return header

    def primeFactors(self, n):
        c = 2
        step = 0
        str_primef = ""
        multi_primef = ""
        # expo_primef = ""
        primef = []
        left = []
        while n > 1:
            step = step + 1
            if n % c == 0:
                # print(c, end=" ")
                primef.append(c)
                left.append(int(n))
                # str_primef = str_primef+f"{c}, "
                # multi_primef = multi_primef + f"{c} x "
                # expo_primef = expo_primef + f"{c}<sup>1</sup> x "
                n = n / c
            else:
                c = c + 1
        left.append(1)
        return primef, left

    def image_upload(self, path):
        header = self.authenticate()
        url = 'https://calculator4engineers.com/wp-json/wp/v2'
        media = {'file': open(path, 'rb')}
        image = requests.post(url+'/media', headers=header, files=media)
        post_id = json.loads(image.content.decode('utf-8'))['id']
        image_link = image.json()['guid']['rendered']
        locString = f"<!-- wp:image {{\"id\":{str(post_id)},\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
        locString += f"<figure class=\"wp-block-image size-full\"><img src=\"{image_link}\" alt=\"\" class=\"wp-image-{str(post_id)}\"/></figure>"
        locString += "<!-- /wp:image -->"
        code = locString
        return code

    def link_previous(self, numbers, index):
        code = wp_paragraph(
            "<strong> Check the first step of these prime factorization examples to better understand how this step is done:</strong>")
        if index == 0:
            pass
        elif index == 1:
            code += f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-1]}/\">Prime factorization of {numbers[index-1]}</a></li></ul><!-- /wp:list -->"
        elif index == 2:
            code += f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-1]}/\">Prime factorization of {numbers[index-1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-2]}/\">Prime factorization of {numbers[index-2]}</a></li></ul><!-- /wp:list -->"
        else:
            code += f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-1]}/\">Prime factorization of {numbers[index-1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-2]}/\">Prime factorization of {numbers[index-2]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-3]}/\">Prime factorization of {numbers[index-3]}</a></li></ul><!-- /wp:list -->"
        return code

    def link_next(self, numbers, index):
        code = wp_paragraph(
            "<strong>Check the first step of these prime factorization examples to better understand how this step is done:</strong>")
        if len(numbers)-1 == index:
            pass
        elif index == len(numbers)-2:
            code += f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+1]}/\">Prime factorization of {numbers[index+1]}</a></li></ul><!-- /wp:list -->"
        elif index == len(numbers)-3:
            code += f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+1]}/\">Prime factorization of {numbers[index+1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+2]}/\">Prime factorization of {numbers[index+2]}</a></li></ul><!-- /wp:list -->"
        else:
            code += f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+1]}/\">Prime factorization of {numbers[index+1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+2]}/\">Prime factorization of {numbers[index+2]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+3]}/\">Prime factorization of {numbers[index+3]}</a></li></ul><!-- /wp:list -->"

        return code

    def wp_h3(self, text):
        return f"<!-- wp:heading {{\"level\":3}} --><h3>{text}</h3><!-- /wp:heading -->"

    def wp_h4(self, text):
        return f"<!-- wp:heading {{\"level\":4}} --><h4>{text}</h4><!-- /wp:heading -->"

    def wp_paragraph(self, text):
        return f"<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->"

    def factorTreeSteps(self):
        n = self.n
        # index = self.index

        primef, left = self.primeFactors(n)
        initialStep = []
        initialStepBy2 = []
        initialStepNotBy2 = []
        lastStep = []
        treeImages = self.treeImages
        content = ""

######################################INITIAL STEP#########################################################################

        initialStep.append(
            f"Before we can begin to factor a given number, we need to write it down. {n} is the given number in this context. Get the first two factors of the number {n}. We'll begin with the smallest possible number, which is 2 (Note that we didn't pick 1, since every integer is divisible by both 1 and itself).<br>")
        initialStep.append(
            f"Let’s take {n} as our given number. Now, we’ll write the root first. Then we’ll draw two arrows to link the first to branches or factors with the root. We’ll start trying from 2 and continue until we find a number that divides {n} exactly.<br>")
        initialStep.append(
            f"{n} is the given number whose factors are to be found. We’ll try to find its smallest factor which isn’t 1 as 1 is the divisor of every number & it isn’t a prime number. So let's begin with number 2.<br>")
        initialStep.append(f"Let's use the given number, {n}. We'll now start by writing the root. Then, we'll draw two arrows to connect the first to the root's branches or contributing elements. Starting with 2, we'll keep trying until we find a number that divides {n} perfectly. (Note that we didn't take 1 because every number can be divided by both 1 and the number itself).<br>")
        initialStep.append(f"{n} is the targeted number whose factors are to be determined. We have to find the first two factors of {n}. We'll find if 2 is a factor of {n} because 2 is the smallest possible number we have in our hand(Note that we didn't pick 1, since 1 and the number itself are always the two factors of the given number).<br>")
        initialStep.append(
            f"The target number, for which the factors should be determined, is {n}. We'll try to find such two numbers which we can multiply to get {n} . But we won't use 1 because if we use 1, we have to multiply it with {n} to obtain {n} and it won't decompose our given number. So, we'll check if 2 is a factor of {n} since it's the smallest integer we can use.<br>")

######################################INITIAL STEP DIVIDED BY 2#########################################################################

        initialStepBy2.append(
            f"With no leftover, {n} is divided by 2 in this instance.Therefore, the first two factors of {n} will be {primef[0]} and {left[1]}.We would continue exploring until we discovered a prime number that exactly divided {n} if it wasn't divisible by 2. ")
        initialStepBy2.append(
            f"There are no leftovers when you split {n} by 2. Thus, {primef[0]} and {left[1]} will be the first two elements of {n}. If it wasn't divisible by 2, we would keep looking until we found a prime number that exactly divided {n}. ")
        initialStepBy2.append(
            f"Here {n} is divided by 2, leaving no remainder. The first two components of {n} will thus be {primef[0]} and {left[1]}. If it wasn't divisible by 2, we would keep looking until a prime number was found that exactly divided {n}. ")

######################################INITIAL STEP NOT DIVIDED BY 2#########################################################################

        initialStepNotBy2.append(
            f"Yet {n} cannot be divided by 2 without remainder. We'll give it a shot with {primef[0]}, since {n} is neatly divisible by that number. If it wasn't divisible by {primef[0]}, we'd keep looking until we found a prime number that exactly divided {n}. We’ll get {primef[0]} & {left[1]} as the first two factors of {n}. ")
        initialStepNotBy2.append(
            f"{primef[0]} divides {n} exactly and we get {primef[0]} & {left[1]} as two factors of {n}.")
        initialStepNotBy2.append(
            f"{n} isn’t evenly divisible by 2. So, we’ll try with {primef[0]} and it is exactly divisible by {primef[0]} giving {primef[0]} & {left[1]} as the two factors of {n}. (Note: If it wasn’t divisible by {primef[0]}, we would’ve gone to the next number until we find the number which divides {n} exactly.) ")
        initialStepNotBy2.append(
            f"Yet {n} cannot be divided by 2 without remainder. {primef[0]} divides {n} perfectly, giving us {primef[0]} and {left[1]} as two factors.")
        initialStepNotBy2.append(
            f"But 2 isn’t a factor of {n}. We'll give it a shot with {primef[0]}, since {n} is evenly divisible by that number, it is a factor of {n} along with {left[1]}. If it wasn't {primef[0]}, we'd keep looking until we found our first two factors of {n}.")
        initialStepNotBy2.append(
            f"Without a remainder, {n} cannot be divided by 2. Since {n} is easily divisible by {primef[0]}, we'll give it a go with {primef[0]} (Note: we would have to continue exploring until we found a prime number that exactly divided {n}). So, as the first two factors of {n}, we'll obtain {primef[0]} and {left[1]}.")

######################################LOOP INSIDE RANDOM STRING#########################################################################

        # loopInsideRandomString.append(
        #     f"Given that 3 is prime whereas 3455 is not, we can factorize 3455 in the same way we did before. The two components of 3455 are hence 5 and 691.")

        h4_step = "Step 1"
        content += self.wp_h4(h4_step)
        content += self.image_upload(treeImages[0])

        if primef[0] == 2:
            content += self.wp_paragraph(random.choice(initialStep) +
                                         random.choice(initialStepBy2))
        else:
            content += self.wp_paragraph(random.choice(initialStep) +
                                         random.choice(initialStepNotBy2))

        if len(primef) > 1:
            for j in range(1, len(primef)-1):
                h4_step = f"Step {j+1}"
                content += self.wp_h4(h4_step)
                content += self.image_upload(treeImages[j])

                loopInsideRandomString = [
                    f"Given that {primef[j-1]} is prime whereas {left[j]} is not , we can factorize {left[j]} in the same way we did before. The two components of {left[j]} are hence {primef[j]} and {left[j+1]}.",
                    f"As {primef[j-1]} is also a prime number, and so, we only need to find the next two factors of {left[j]}. The two factors of {left[j]} are {primef[j]} & {left[j+1]}.",
                    f"As {primef[j-1]} is a prime number but {left[j]} isn’t, we’ll factorize {left[j]} like the previous one. We’ll get {primef[j]} and {left[j+1]} as the two factors of {left[j]}.",
                    f"Since {primef[j-1]} is also a prime number, only the next two factors of {left[j]} need to be determined. The two factors of {left[j]} are {primef[j]} & {left[j+1]}.",
                    f"As {primef[j-1]} is a prime number, it is also our first prime factor. Whereas {left[j]} is not , so we’ve to factorize {left[j]} in the same way we did it for {left[j-1]}. The two components of {left[j]} are hence {primef[j]} and {left[j+1]}.",
                    f"{primef[j-1]} is a prime number but {left[j]} is not. Thus we must factorize it similarly to how we did for {left[j-1]}. Thus, {primef[j]} & {left[j+1]} are the two factors of {left[j]}."
                ]
                content += random.choice(loopInsideRandomString)

        return content
