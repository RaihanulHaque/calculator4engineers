# from primeFactorVisualizer import generateImages
# import random

# n = 78275
# arr = createTreeStructure(n)
# arr.pop()
# arr.append(createNormalStructure(n)[0])
# image_list = generateImages(n)['Banners']
# random_image = random.choice(image_list)
# print(image_list)
# image_link = "Rahi"
# code = '<!-- wp:image {"id":'+str(123)+',"sizeSlug":"large","linkDestination":"none"} - ->< figure class = "wp-block-image size-large" > <img src =\'' + \
#     image_link + '\' alt = "Prime Factorial" class = "wp-image-' + \
#     str(123)+'"/> < /figure ><!-- / wp: image - ->'

# print(code[0])
# cont = <!-- wp: paragraph {"align": "center"} - -> < p class = "has-text-align-center" > <strong > Baka < /strong > </p > <!-- / wp: paragraph - ->
# , \"sizeSlug\": \"full\", \"linkDestination\": \"none\"
# text = "Rahi"
# baka = f"<!-- wp:paragraph {{\"align\":\"center\"}} --><p class = \"has-text-align-center\" ><strong>{text}< /strong > </p > <!-- / wp: paragraph - ->"
# print(baka)

# def wp_paragraph_center(text):
#     return f"<!-- wp:paragraph {{\"align\":\"center\"}} --><p class = \"has-text-align-center\" ><strong>{text}< /strong > </p > <!-- / wp: paragraph - ->"


# def wp_h4(text):
#     return f"<!-- wp:heading {{\"level\":4}} --><h4>{text}</h4><!-- /wp:heading -->"


# print(wp_h4("Rahi"))
# from math import sqrt
# n = 10365
# for x in range(1, int(sqrt(n))+1):
#     if n % x == 0:
#         print(f"{x}   {int(n/x)}\n")

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


primef = [2, 2, 4, 5, 5, 5]
array = exponential(primef)
# for key in array:
#     print(f"{key} {array[key]}")
print(array)
