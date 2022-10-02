from primeFactorVisualizer import generateImages
import random

n = 78275
# arr = createTreeStructure(n)
# arr.pop()
# arr.append(createNormalStructure(n)[0])
image_list = generateImages(n)['Banners']
# random_image = random.choice(image_list)
print(image_list)
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
