
from primeFactorVisualizer import generateImages
from datetime import timedelta, datetime
import random
import json
import base64
import requests
from math import sqrt, floor


def authenticate():
    user = "Rahi"
    password = "t5nC 34nz obVc BUzM c1Nt KQnK"
    creds = user + ':' + password
    cred_token = base64.b64encode(creds.encode())
    header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
    return header


def primeFactors(n):
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
            str_primef = str_primef+f"{c}, "
            multi_primef = multi_primef + f"{c} x "
            # expo_primef = expo_primef + f"{c}<sup>1</sup> x "
            n = n / c
        else:
            c = c + 1
    left.append(1)
    return primef, left, str_primef[:-2], multi_primef[:-2]


def exponential(array):
    frequency = {}
    str = ""
    for item in array:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    for key in frequency:
        str += f"{key}<sup>{frequency[key]}</sup> x "

    return str[:-3]


def featured_image_upload(image_list):
    path = random.choice(image_list)
    media = {'file': open(path, 'rb')}
    image = requests.post(url+'/media', headers=header, files=media)
    post_id = json.loads(image.content.decode('utf-8'))['id']
    return post_id


def image_upload(path):
    media = {'file': open(path, 'rb')}
    image = requests.post(url+'/media', headers=header, files=media)
    post_id = json.loads(image.content.decode('utf-8'))['id']
    image_link = image.json()['guid']['rendered']
    locString = f"<!-- wp:image {{\"id\":{str(post_id)},\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
    locString += f"<figure class=\"wp-block-image size-full\"><img src=\"{image_link}\" alt=\"\" class=\"wp-image-{str(post_id)}\"/></figure>"
    locString += "<!-- /wp:image -->"
    code = locString
    return code


def image_add_tree():
    locString = f"<!-- wp:image {{\"id\":452,\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
    locString += f"<figure class=\"wp-block-image size-full\"><img src=\"https://calculator4engineers.com/wp-content/uploads/2022/10/treefact.jpg\" alt=\"\" class=\"wp-image-452\"/></figure>"
    locString += "<!-- /wp:image -->"
    return locString


def image_add_division():
    locString = f"<!-- wp:image {{\"id\":471,\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
    locString += f"<figure class=\"wp-block-image size-full\"><img src=\"https://calculator4engineers.com/wp-content/uploads/2022/10/unnamed.jpg\" alt=\"\" class=\"wp-image-471\"/></figure>"
    locString += "<!-- /wp:image -->"
    return locString


def wp_paragraph(text):
    return f"<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->"


def wp_h2(text):
    return f"<!-- wp:heading {{\"level\":2}} --><h2>{text}</h2><!-- /wp:heading -->"


def wp_h3(text):
    return f"<!-- wp:heading {{\"level\":3}} --><h3>{text}</h3><!-- /wp:heading -->"


def wp_h4(text):
    return f"<!-- wp:heading {{\"level\":4}} --><h4>{text}</h4><!-- /wp:heading -->"


def wp_paragraph_center(text):
    return f"<!-- wp:paragraph {{\"align\":\"center\"}} --><p class = \"has-text-align-center\" >{text}</p> <!-- /wp: paragraph -->"


def wp_table(text):
    return f"<!-- wp:table {{\"hasFixedLayout\":true,\"className\":\" is -style-stripes prime-factorization-table\"}} --><figure class=\"wp-block-table is-style-stripes prime-factorization-table\"><table class=\"has-fixed-layout\"><tbody>{text}</tbody></table><figcaption>Prime Factorization of 10365</figcaption></figure><!-- /wp:table -->"


def link_previous(numbers, index):
    code = wp_paragraph(
        "<strong> Check the first step of these prime factorization examples to better understand how this step is done:</strong>")
    if index == 0:
        pass
    elif index == 1:
        code = code + \
            f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-1]}/\">Prime factorization of {numbers[index-1]}</a></li></ul><!-- /wp:list -->"
    elif index == 2:
        code = code + \
            f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-1]}/\">Prime factorization of {numbers[index-1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-2]}/\">Prime factorization of {numbers[index-2]}</a></li></ul><!-- /wp:list -->"
    else:
        code = code + \
            f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-1]}/\">Prime factorization of {numbers[index-1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-2]}/\">Prime factorization of {numbers[index-2]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index-3]}/\">Prime factorization of {numbers[index-3]}</a></li></ul><!-- /wp:list -->"
    return code


def link_next(numbers, index):
    code = wp_paragraph(
        "<strong>Check the first step of these prime factorization examples to better understand how this step is done:</strong>")
    if len(numbers)-1 == index:
        pass
    elif index == len(numbers)-2:
        code = code + \
            f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+1]}/\">Prime factorization of {numbers[index+1]}</a></li></ul><!-- /wp:list -->"
    elif index == len(numbers)-3:
        code = code + \
            f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+1]}/\">Prime factorization of {numbers[index+1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+2]}/\">Prime factorization of {numbers[index+2]}</a></li></ul><!-- /wp:list -->"
    else:
        code = code + \
            f"<!-- wp:list --><ul><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+1]}/\">Prime factorization of {numbers[index+1]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+2]}/\">Prime factorization of {numbers[index+2]}</a></li><li><a href=\"https://calculator4engineers.com/prime-factorization/prime-factorization-of-{numbers[index+3]}/\">Prime factorization of {numbers[index+3]}</a></li></ul><!-- /wp:list -->"

    return code


def nearestPrime(n):
    if (n & 1):
        n -= 2
    else:
        n -= 1
    i, j = 0, 5
    for i in range(n, 2, -2):
        if (i % 2 == 0):
            continue
        while (j <= floor(sqrt(i)) + 1):
            if (i % j == 0):
                break
            j += 2
        if (j > floor(sqrt(i))):
            return i
    # It will only be executed when n is 3
    return 2


def check_squared(n):
    root = sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return f"Yes. The square root of {n} is an integer. So it is a square number."
    else:
        return f"No. The square root of {n} isn’t an integer. So it isn’t a square number."


def isPrime_or_Composite(n):
    primef, left, str_primef, multi_primef = primeFactors(n)
    if len(primef) > 1:
        return f"{n} is a composite number."
    else:
        return f"{n} is a prime number."


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


url = 'https://calculator4engineers.com/wp-json/wp/v2'
header = authenticate()
current_time = datetime.now()
numbers = [320, 10365, 46, 54, 69, 104, 326]
for i in range(0, len(numbers)):
    n = numbers[i]
    treeImages = generateImages(n)['TreeFiles']
    divisionImages = generateImages(n)['DivisionFiles']
    bannerImages = generateImages(n)['Banners']
    primef, left, str_primef, multi_primef = primeFactors(n)
    content = ""
    ################################################################################
    #############################################################################################
    # Introduction
    #############################################################################################
    content = content + f"<!-- wp:paragraph --><p>{multi_primef}= {n}. So, the prime factors of {n} are {str_primef}.</p><!-- /wp:paragraph --><!-- wp:paragraph --><p>{n} can be written as the product of {str_primef}. So {str_primef} are the <strong>factors</strong> of {n}. They are <strong>prime numbers</strong> as well. Thus {str_primef} become the <strong>prime factors</strong> of {n}.</p><!-- /wp:paragraph -->"
    content = content + wp_table(f"<tr><td>Prime Factors</td><td>{str_primef}</td></tr><tr><td>Product of Prime Factor</td><td>{multi_primef}</td></tr><tr><td>Exponential Form</td><td>{exponential(primef)}</td></tr><tr><td>Total Number of Factors</td><td>{len(primef)}</td></tr><tr><td>Largest Prime Factor</td><td>{max(primef)}</td></tr><tr><td>Smallest Prime Factor</td><td>{min(primef)}</td></tr><tr><td>Closest Prime Numbers</td><td>{nearestPrime(n)}</td></tr>")
    content = content + wp_h2("Prime Factors by Definition")
    # content = content + f"<!-- wp:paragraph --><p>Factors are those integers which divide a number evenly and the remainder is <strong>0</strong>. Or we can think the other way, if we multiply two numbers to get a product, then, those two numbers are the factors of that product. Factor is always an integer number. It can’t be a fraction.&nbsp;</p><!-- /wp:paragraph -->"
    content = content + wp_paragraph("The term <strong>factors</strong> indicate those integers which divide a number in such a way that the remainder becomes <strong>0</strong>. Contrarily, the multipliers of a product can be depicted as the factors of that product. But remember, a factor mustn’t be a fraction number. So, we can use only the integers as the multipliers. If the factors of a number are prime numbers, then they are called <strong>prime factors</strong>.")
    # content = content + f"<!-- wp:paragraph --><p>If the factors of a number are prime numbers, then they are called <strong>prime</strong> factors. The process of determining factors is known as factorization. And if it only determines the prime numbers, then it can be called&nbsp; prime factorization.</p><!-- /wp:paragraph -->"
    content = content + wp_paragraph_center("105 = 3x5x7")

    content = content + \
        wp_paragraph(
            "Here, 105 is the product of multiplication of 3, 5, 7. All the multipliers are prime numbers. So, 3, 5, 7 are the prime factors of 105.")
    content = content + wp_h2("What is Factorization?")
    content = content + \
        wp_paragraph(
            "The process of determining factors is known as factorization.")
    content = content + wp_h2("What is Prime Factorization?")
    content = content + \
        wp_paragraph(
            "Prime factorization is a type of factorization where we determine only those factors which are prime numbers.")
    content = content + wp_h2("Formula of Prime Factor")
    content = content + \
        wp_paragraph(
            "It is possible to write any composite number as the product of powers of prime numbers. When a number is written as the product of multiple prime numbers, the process is called prime factorization. Mathematical expression for prime factors:")
    content = content + \
        wp_paragraph(
            "N = p<sub>f1</sub><sup>a1</sup> +&nbsp; p<sub>f2</sub><sup>a2</sup> +&nbsp; &nbsp; p<sub>f3</sub><sup>a3</sup> + ... ... +&nbsp; p<sub>fn</sub><sup>an</sup>")
    content = content + wp_paragraph("N = Any integer number")
    content = content + \
        wp_paragraph(
            "p<sub>f1</sub>, p<sub>f2</sub>, p<sub>f3</sub>, p<sub>fn</sub> = Prime factors")
    content = content + \
        wp_paragraph(
            "a<sub>1</sub> ,a<sub>2</sub>, a<sub>3</sub>, a<sub>n</sub>&nbsp; = Orders of prime factors")
    content = content + wp_h2(f"How to Calculate the Prime Factors of {n}?")
    content = content + \
        wp_paragraph(
            "Prime factors can be determined in several ways. Two of the most common methods are:")
    content = content + f"<!-- wp:list --><ul><li>Factor tree method.</li><li>Division method.</li></ul><!-- /wp:list -->"

    #############################################################################################
    # Factor Tree Method
    #############################################################################################

    content = content + wp_h3("Factor Tree Method")
    content = content + \
        wp_paragraph("Here, the target number serves as the tree's root, while the factors are its branches. For this reason, we refer to it as the Factor Tree Approach.")
    content = content + image_add_tree()
    content = content + wp_paragraph("In this case, we'll represent the supplied number as the root of a tree and its factors as their respective branches. We'll use diagonals to graphically represent the relationship between the two variables and the tree structures. We'll extract just prime factors from the tree. By breaking it down into manageable chunks, we can accomplish it.")

    h4_step = "Step 1"
    content = content + wp_h4(h4_step)
    hold = f"Before we can begin to factor a given number, we need to write it down. {n} is the given number in this context. Get the first two factors of the number {n}. We'll begin with the smallest possible number, which is 2 (Note that we didn't pick 1, since every integer is divisible by both 1 and itself). <br>"
    if primef[0] == 2:
        content = content + \
            wp_paragraph(
                hold + f"With no leftover, {n} is divided by 2 in this instance.Therefore, the first two factors of {n} will be {primef[0]} and {left[1]}.We would continue exploring until we discovered a prime number that exactly divided {n} if it wasn't divisible by 2. ") + image_upload(treeImages[0])
    else:
        content = content + \
            wp_paragraph(
                hold + f"Yet {n} cannot be divided by 2 without remainder. We'll give it a shot with {primef[0]}, since {n} is neatly divisible by that number. If it wasn't divisible by {primef[0]}, we'd keep looking until we found a prime number that exactly divided {n}. We’ll get {primef[0]} & {left[1]} as the first two factors of {n}. ") + image_upload(treeImages[0])
    # content = content + link_previous(numbers, i)
    content = content + link_previous(numbers, i)
    if len(primef) > 1:
        for j in range(1, len(primef)-1):
            h4_step = f"Step {j+1}"
            random_list = [f"Given that {primef[j-1]} is prime whereas {left[j]} is not , we can factorize {left[j]} in the same way we did before. The two components of {left[j]} are hence {primef[j]} and {left[j+1]}.", f"We can factorize {left[j]} the same way we did previously because {primef[j-1]} is prime but {left[j]} is not . Thus, {primef[j]} and {left[j+1]} are the two parts of {left[j]}. ", f"Since {left[j]} is not prime but {primef[j-1]} is , we can factorize {left[j]} in the same manner as before.{primef[j]} and {left[j+1]} are the two parts of {left[j]} as a result. "
                           f"We'll now carry out the same exact procedure for the quotient as well. This time, the quotient will be {left[j+1]} when we divide {left[j]} by {primef[j]}. ", f"The exact same procedure will now be repeated for the quotient as well. This time, the result of dividing {left[j]} by {primef[j]} is {left[j+1]}. "]
            content = content + wp_h4(h4_step) + \
                wp_paragraph(random.choice(random_list)) + \
                image_upload(treeImages[j])

        h4_step = f"Step {len(primef)}"
        random_list = [f"Since {primef[len(primef)-2]} and {left[len(primef)-1]} are both prime numbers, it cannot be factored any further. With that, our factor tree is finished.", f"There are no more factors because {primef[len(primef)-2]} and {left[len(primef)-1]} are both prime numbers. Our factor tree is now complete. ", f"It cannot be further factored because {primef[len(primef)-2]} and {left[len(primef)-1]} are both prime numbers. Our factor tree is complete at this point. ", f"At last being a prime, {left[len(primef)-1]} can be evenly divided only by itself and the quotient will become 1. So our tree is complete ",
                       f"Due to its prime nature, {left[len(primef)-1]} can only be evenly divided by itself and {primef[len(primef)-2]} is a prime number, in which case the quotient will be 1. Thus the tree is complete.", f"At last {primef[len(primef)-2]} is a prime number and {left[len(primef)-1]} is only divisible by {primef[len(primef)-1]} which is a prime number. So it can’t be factorized again. So, our factor tree is completed."]
        content = content + wp_h4(h4_step) + \
            wp_paragraph(random.choice(random_list))

    content = content + \
        wp_paragraph(
            f"From the diagram we get {str_primef} as the prime factors of {n} as those factors can’t be factorized further.")
    content = content + \
        wp_paragraph(f"We can express like this: {n} = {multi_primef}")
    content = content + \
        wp_paragraph(
            "<b> Note: we need to factorize them until all the factors become prime numbers.</b>")

    #############################################################################################
    # Division Method
    #############################################################################################

    content = content + wp_h3("Division Method")
    content = content + wp_paragraph("To find prime factors, you can also use another well-known technique. The process is known as division. Finding factors in this manner is the least complicated option.This approach requires repeated division by the specified number.")
    content = content + image_add_division()
    content = content + \
        wp_paragraph(
            "That's why it's referred to as a \"division method.\" Here's how it works, step by step:")

    h4_step = "Step 1"
    content = content + wp_h4(h4_step)
    hold = f"Let’s find out the prime factors of {n} by division method. First we’ll divide the {n} by the smallest prime number 2. "
    if primef[0] == 2:
        content = content + \
            wp_paragraph(
                hold + f"We can divide {n} by 2 easily. Then, we have to move towards the next one. {primef[1]} can divide {left[1]} evenly. So, we’ll divide it by {primef[1]} and get {left[2]} as the quotient.") + image_upload(divisionImages[0])
        phase2 = 2
        content = content + link_next(numbers, i)
        if len(primef) > 2:
            for j in range(phase2, len(primef)-1):
                h4_step = f"Step {j}"
                # random_list = [f"Now {left[i]} is divisible by {primef[i]} which is a prime number and the reminder is {left[i+1]}", f"Here the prime number {primef[i]} divides {left[i]}, and the reminder is {left[i+1]}",
                #                f"The reminder in this case is {left[i+1]}, and the number {left[i]} is divisible by {primef[i]} - a prime number"]
                random_list = [
                    f"Now we’ll repeat the exact process for the quotient also. We can divide {left[j]} by {primef[j]} and {left[j+1]} will be the quotient this time. ", f"We'll now carry out the same exact procedure for the quotient as well. This time, the quotient will be {left[j+1]} when we divide {left[j]} by {primef[j]}. ", f"We'll do the same exact thing for the quotient next. We may divide {left[j]} by {primef[j]}, and this time the quotient will be {left[j+1]}. ", f"The exact same procedure will now be repeated for the quotient as well. This time, the result of dividing {left[j]} by {primef[j]} is {left[j+1]}. "]
                content = content + wp_h4(h4_step) + \
                    wp_paragraph(random.choice(random_list)) + \
                    image_upload(divisionImages[j])
            h4_step = f"Step {len(primef)-1}"
            random_list = [f"Being a prime, {left[len(primef)-1]} can be evenly divided only by itself and the quotient will become 1. ", f"Being a prime, {left[len(primef)-1]} can only be evenly divided by itself, resulting in a fraction of 1. ",
                           f"Due to its prime nature, {left[len(primef)-1]} can only be evenly divided by itself, in which case the quotient will be 1. ", f"Now {left[len(primef)-1]} can only be evenly divided by itself because it is a prime number, and the result is 1. ", f"At last {left[len(primef)-1]} is only divisible by {primef[len(primef)-1]} which is a prime number. So it can’t be factorized again. So, our factor tree is completed."]
            content = content + wp_h4(h4_step) + \
                wp_paragraph(random.choice(random_list)) + \
                image_upload(divisionImages[len(divisionImages)-1])
    else:
        content = content + \
            wp_paragraph(
                hold + f"But 2 can’t divide {n} exactly. So, we have to move towards the next one. {primef[0]} can divide {n} evenly. So, we’ll divide it by {primef[0]} and get {left[1]} as the quotient.") + image_upload(divisionImages[0])
        phase2 = 1
        content = content + link_next(numbers, i)
        if len(primef) > 1:
            for j in range(phase2, len(primef)-1):
                h4_step = f"Step {j+1}"
                # random_list = [f"Now {left[i]} is divisible by {primef[i]} which is a prime number and the reminder is {left[i+1]}", f"Here the prime number {primef[i]} divides {left[i]}, and the reminder is {left[i+1]}",
                #                f"The reminder in this case is {left[i+1]}, and the number {left[i]} is divisible by {primef[i]} - a prime number"]
                random_list = [
                    f"Now we’ll repeat the exact process for the quotient also. We can divide {left[j]} by {primef[j]} and {left[j+1]} will be the quotient this time. ", f"We'll now carry out the same exact procedure for the quotient as well. This time, the quotient will be {left[j+1]} when we divide {left[j]} by {primef[j]}. ", f"We'll do the same exact thing for the quotient next. We may divide {left[j]} by {primef[j]}, and this time the quotient will be {left[j+1]}. ", f"The exact same procedure will now be repeated for the quotient as well. This time, the result of dividing {left[j]} by {primef[j]} is {left[j+1]}. "]
                content = content + wp_h4(h4_step) + \
                    wp_paragraph(random.choice(random_list)) + \
                    image_upload(divisionImages[j])

            h4_step = f"Step {len(primef)}"
            random_list = [f"Being a prime, {left[len(primef)-1]} can be evenly divided only by itself and the quotient will become 1. ", f"Being a prime, {left[len(primef)-1]} can only be evenly divided by itself, resulting in a fraction of 1. ",
                           f"Due to its prime nature, {left[len(primef)-1]} can only be evenly divided by itself, in which case the quotient will be 1. ", f"Now {left[len(primef)-1]} can only be evenly divided by itself because it is a prime number, and the result is 1. ", f"At last {left[len(primef)-1]} is only divisible by {primef[len(primef)-1]} which is a prime number. So it can’t be factorized again. So, our factor tree is completed."]
            content = content + wp_h4(h4_step) + \
                wp_paragraph(random.choice(random_list)) + \
                image_upload(divisionImages[len(divisionImages)-1])
    content = content + \
        wp_paragraph(
            "<strong> Note: We’ll have to repeat the process until the quotient becomes 1.</strong>")
    #############################################################################################
    # Golpo
    #############################################################################################
    # content = content + wp_h2(f"Closest Prime Number of {n}")
    # content = content + \
    #     wp_paragraph(f"The closest prime number is {nearestPrime(n)}")
    holdarr = []
    holdarrstr1 = ""
    holdarrstr2 = ""
    extracode = ""
    for x in range(1, int(sqrt(n))+1):
        if n % x == 0:
            extracode = extracode + wp_paragraph(f"{n} ÷ {x} = {int(n/x)}")
            holdarr.append(x)
            holdarr.append(int(n/x))

    holdarr.sort()
    for y in range(0, len(holdarr)):
        holdarrstr1 = holdarrstr1 + f"{holdarr[y]}, "
        holdarrstr2 = holdarrstr2 + f"-{holdarr[y]}, "

    content = content + wp_h2(f"Non-Prime Factors of {n}")
    nonPrimefact = ""
    for x in range(0, len(primef)):
        if primef[x] in holdarr:
            holdarr.remove(primef[x])
    for x in range(0, len(holdarr)):
        nonPrimefact = nonPrimefact + f"{holdarr[x]}, "
    content = content + \
        wp_paragraph(
            f"All the positive factors of {n} are {holdarrstr1[:-2]}. So, the non-prime factors are {nonPrimefact[:-2]}.")
    # content = content + wp_paragraph(text)

    content = content + wp_h2(f"Negative Factors of {n}")
    content = content + \
        wp_paragraph(
            f"The negative factors of {n} are {holdarrstr2[:-2]}.")
    content = content + wp_h2(f"How to Determine All the Factors of {n}?")
    content = content + \
        wp_paragraph(
            f"To determine all the factors of 10365, we have to find every divisor that divides {n} exactly. After finding that, we should express this like this:")
    content = content + extracode
    content = content + \
        wp_paragraph(f"Here every divisor & quotient are the factors of {n}.")

    content = content + \
        wp_paragraph(
            f"So, the positive factors of {n} are: {holdarrstr1[:-2]}.")

    content = content + wp_paragraph("We can also express this like:")
    for x in range(1, int(sqrt(n))+1):
        if n % x == 0:
            content = content + wp_paragraph(f"-{int(n/x)} x -{x} = {n}")
    content = content + \
        wp_paragraph(
            f"So the negative factors are: {holdarrstr2[:-2]}.")
    #############################################################################################
    content = content + wp_h2("Facts of Factorization")
    content = content + f"<!-- wp:list --><ul><li>No fractional parts of numbers can be used as factors.</li><li> The number you enter must be a whole number.</li><li>Factors can be both negative & positive.</li><li>Each and every natural number has 1 as a factor.</li><li>It is also possible to factor a quadratic equation.</li></ul> <!-- / wp:list -->"

    content = content + wp_h2("Use of Factors")
    content = content + wp_paragraph("Factors allow us to put things in various configurations. It's useful for making fair divisions. It has several applications in mathematics involving numbers. The ability to do so is also helpful when making comparisons, exchanging money, telling time, etc. Quadratic equations can also be factored to make solving them easier.")
    content = content + \
        wp_paragraph(
            "Remember, a negative factor must multiply with another negative factor only to get our given number.")
    #############################################################################################
    # Frequently Asked Questions
    #############################################################################################
    content = content + wp_h2("Frequently Asked Questions")
    content = content + wp_h3("Can Factors Be Negative?")
    content = content + wp_paragraph("Yes. Factors can be negative too. Like the factors of 10 are 1, 2, 5, 10, -1, -2, -5, -10. Because if we multiply - 10 with -1, we’ll get 10. So, -10 & -1 are the factors of 10. But most of the time we use positive factors only.")
    content = content + wp_h3(f"2. Is {n} a Square Number?")
    content = content + wp_paragraph(f"{check_squared(n)}")
    content = content + wp_h3(f"3. What is the square of {n}?")
    content = content + wp_paragraph(f"Square of {n} is {n*n}.")
    content = content + wp_h3(f"4. What is the root of {n}?")
    content = content + wp_paragraph(f"Root of {n} is {sqrt(n)}")
    content = content + \
        wp_h3(f"5. Is {n} a Composite Number or a Prime Number?")
    content = content + wp_paragraph(f"{isPrime_or_Composite(n)}")
    content = content + wp_h3("6. How Many Factors Does a Prime Number Have?")
    content = content + \
        wp_paragraph(
            "A Prime number has only 2. They are 1 &amp; the number itself.")
    content = content + wp_h3("7. What is a Composite Number?")
    content = content + \
        wp_paragraph(
            "If a positive integer number has more than two factors, it can be called a composite number.")
    content = content + wp_h3("8. What are the factors of a prime number?")
    content = content + wp_paragraph("They are 1 & the number itself.")
    #################################################################################################################

    #############################################################################################
    # REST API Post to Wordpress
    #############################################################################################
    tdelta = timedelta(minutes=random.randrange(3, 7))
    current_time = current_time + tdelta
    time = schedule(current_time)
    #############################################################################################
    post = {
        'title': f"Prime Factorization of {n}",
        # 'slug': postslug,
        'content': content,
        'status': 'publish',
        'author': random.choice(['1', '2', '4', '5', '6']),
        'publish': 'standard',
        'date': time,
        'categories': '4',
        'featured_media': str(featured_image_upload(bannerImages))
    }
    wprequest = requests.post(url + '/posts', headers=header, json=post)
    print(f"Number - {i+1} is scheduled at {time}")
