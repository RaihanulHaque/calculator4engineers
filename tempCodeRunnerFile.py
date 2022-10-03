content = content + wp_h3("Factor Tree Method")
# content = content + \
#     wp_paragraph("Here, the target number serves as the tree's root, while the factors are its branches. For this reason, we refer to it as the Factor Tree Approach.")
# content = content + image_add_tree()
# content = content + wp_paragraph("In this case, we'll represent the supplied number as the root of a tree and its factors as their respective branches. We'll use diagonals to graphically represent the relationship between the two variables and the tree structures. We'll extract just prime factors from the tree. By breaking it down into manageable chunks, we can accomplish it.")

# h4_step = "Step 1"
# content = content + wp_h4(h4_step)
# hold = f"Before we can begin to factor a given number, we need to write it down. {n} is the given number in this context. Get the first two factors of the number {n}. We'll begin with the smallest possible number, which is 2 (Note that we didn't pick 1, since every integer is divisible by both 1 and itself). <br>"
# if primef[0] == 2:
#     content = content + \
#         wp_paragraph(
#             f"With no leftover, {n} is divided by 2 in this instance.Therefore, the first two factors of {n} will be {primef[0]} and {left[1]}.We would continue exploring until we discovered a prime number that exactly divided {n} if it wasn't divisible by 2. ") + image_upload(treeImages[0])
# else:
#     content = content + \
#         wp_paragraph(
#             hold + f"Yet {n} cannot be divided by 2 without remainder. We'll give it a shot with {primef[0]}, since {n} is neatly divisible by that number. If it wasn't divisible by {primef[0]}, we'd keep looking until we found a prime number that exactly divided {n}. We’ll get {primef[0]} & {left[1]} as the first two factors of {n}. ") + image_upload(treeImages[0])
# if len(primef) > 1:
#     for i in range(1, len(primef)-1):
#         h4_step = f"Step {i+1}"
#         random_list = [f"Given that {primef[i-1]} is prime whereas {left[i]} is not , we can factorize {left[i]} in the same way we did before. The two components of {left[i]} are hence {primef[i]} and {left[i+1]}.", f"We can factorize {left[i]} the same way we did previously because {primef[i-1]} is prime but {left[i]} is not . Thus, {primef[i]} and {left[i+1]} are the two parts of {left[i]}. ", f"Since {left[i]} is not prime but {primef[i-1]} is , we can factorize {left[i]} in the same manner as before.{primef[i]} and {left[i+1]} are the two parts of {left[i]} as a result. "
#                        f"We'll now carry out the same exact procedure for the quotient as well. This time, the quotient will be {left[i+1]} when we divide {left[i]} by {primef[i]}. ", f"The exact same procedure will now be repeated for the quotient as well. This time, the result of dividing {left[i]} by {primef[i]} is {left[i+1]}. "]
#         content = content + wp_h4(h4_step) + \
#             wp_paragraph(random.choice(random_list)) + \
#             image_upload(treeImages[i])

#     h4_step = f"Step {len(primef)}"
#     random_list = [f"Since {primef[len(primef)-2]} and {left[len(primef)-1]} are both prime numbers, it cannot be factored any further. With that, our factor tree is finished.", f"There are no more factors because {primef[len(primef)-2]} and {left[len(primef)-1]} are both prime numbers. Our factor tree is now complete. ", f"It cannot be further factored because {primef[len(primef)-2]} and {left[len(primef)-1]} are both prime numbers. Our factor tree is complete at this point. ", f"At last being a prime, {left[len(primef)-1]} can be evenly divided only by itself and the quotient will become 1. So our tree is complete ",
#                    f"Due to its prime nature, {left[len(primef)-1]} can only be evenly divided by itself and {primef[len(primef)-2]} is a prime number, in which case the quotient will be 1. Thus the tree is complete.", f"At last {primef[len(primef)-2]} is a prime number and {left[len(primef)-1]} is only divisible by {primef[len(primef)-1]} which is a prime number. So it can’t be factorized again. So, our factor tree is completed."]
#     content = content + wp_h4(h4_step) + \
#         wp_paragraph(random.choice(random_list))

# content = content + \
#     wp_paragraph(
#         f"From the diagram we get {str_primef} as the prime factors of {n} as those factors can’t be factorized further.")
# content = content + \
#     wp_paragraph(f"We can express like this: {n} = {multi_primef}")
# content = content + \
#     wp_paragraph(
#         "<b> Note: we need to factorize them until all the factors become prime numbers.</b>")


# #############################################################################################
# # Division Method
# #############################################################################################

# content = content + wp_h3("Division Method")
# content = content + wp_paragraph("To find prime factors, you can also use another well-known technique. The process is known as division. Finding factors in this manner is the least complicated option.This approach requires repeated division by the specified number.")
# content = content + image_add_division()
# content = content + \
#     wp_paragraph(
#         "That's why it's referred to as a \"division method.\" Here's how it works, step by step:")

# h4_step = "Step 1"
# content = content + wp_h4(h4_step)
# hold = f"Let’s find out the prime factors of {n} by division method. First we’ll divide the {n} by the smallest prime number 2. "
# if primef[0] == 2:
#     content = content + \
#         wp_paragraph(
#             hold + f"We can divide {n} by 2 easily. Then, we have to move towards the next one. {primef[1]} can divide {left[1]} evenly. So, we’ll divide it by {primef[1]} and get {left[2]} as the quotient.") + image_upload(divisionImages[0])
#     phase2 = 2
#     if len(primef) > 2:
#         for i in range(phase2, len(primef)-1):
#             h4_step = f"Step {i}"
#             # random_list = [f"Now {left[i]} is divisible by {primef[i]} which is a prime number and the reminder is {left[i+1]}", f"Here the prime number {primef[i]} divides {left[i]}, and the reminder is {left[i+1]}",
#             #                f"The reminder in this case is {left[i+1]}, and the number {left[i]} is divisible by {primef[i]} - a prime number"]
#             random_list = [
#                 f"Now we’ll repeat the exact process for the quotient also. We can divide {left[i]} by {primef[i]} and {left[i+1]} will be the quotient this time. ", f"We'll now carry out the same exact procedure for the quotient as well. This time, the quotient will be {left[i+1]} when we divide {left[i]} by {primef[i]}. ", f"We'll do the same exact thing for the quotient next. We may divide {left[i]} by {primef[i]}, and this time the quotient will be {left[i+1]}. ", f"The exact same procedure will now be repeated for the quotient as well. This time, the result of dividing {left[i]} by {primef[i]} is {left[i+1]}. "]
#             content = content + wp_h4(h4_step) + \
#                 wp_paragraph(random.choice(random_list)) + \
#                 image_upload(divisionImages[i])
#         h4_step = f"Step {len(primef)-1}"
#         random_list = [f"Being a prime, {left[len(primef)-1]} can be evenly divided only by itself and the quotient will become 1. ", f"Being a prime, {left[len(primef)-1]} can only be evenly divided by itself, resulting in a fraction of 1. ",
#                        f"Due to its prime nature, {left[len(primef)-1]} can only be evenly divided by itself, in which case the quotient will be 1. ", f"Now {left[len(primef)-1]} can only be evenly divided by itself because it is a prime number, and the result is 1. ", f"At last {left[len(primef)-1]} is only divisible by {primef[len(primef)-1]} which is a prime number. So it can’t be factorized again. So, our factor tree is completed."]
#         content = content + wp_h4(h4_step) + \
#             wp_paragraph(random.choice(random_list)) + \
#             image_upload(divisionImages[len(divisionImages)-1])
# else:
#     content = content + \
#         wp_paragraph(
#             hold + f"But 2 can’t divide {n} exactly. So, we have to move towards the next one. {primef[0]} can divide {n} evenly. So, we’ll divide it by {primef[0]} and get {left[1]} as the quotient.") + image_upload(divisionImages[0])
#     phase2 = 1
#     if len(primef) > 1:
#         for i in range(phase2, len(primef)-1):
#             h4_step = f"Step {i+1}"
#             # random_list = [f"Now {left[i]} is divisible by {primef[i]} which is a prime number and the reminder is {left[i+1]}", f"Here the prime number {primef[i]} divides {left[i]}, and the reminder is {left[i+1]}",
#             #                f"The reminder in this case is {left[i+1]}, and the number {left[i]} is divisible by {primef[i]} - a prime number"]
#             random_list = [
#                 f"Now we’ll repeat the exact process for the quotient also. We can divide {left[i]} by {primef[i]} and {left[i+1]} will be the quotient this time. ", f"We'll now carry out the same exact procedure for the quotient as well. This time, the quotient will be {left[i+1]} when we divide {left[i]} by {primef[i]}. ", f"We'll do the same exact thing for the quotient next. We may divide {left[i]} by {primef[i]}, and this time the quotient will be {left[i+1]}. ", f"The exact same procedure will now be repeated for the quotient as well. This time, the result of dividing {left[i]} by {primef[i]} is {left[i+1]}. "]
#             content = content + wp_h4(h4_step) + \
#                 wp_paragraph(random.choice(random_list)) + \
#                 image_upload(divisionImages[i])

#         h4_step = f"Step {len(primef)}"
#         random_list = [f"Being a prime, {left[len(primef)-1]} can be evenly divided only by itself and the quotient will become 1. ", f"Being a prime, {left[len(primef)-1]} can only be evenly divided by itself, resulting in a fraction of 1. ",
#                        f"Due to its prime nature, {left[len(primef)-1]} can only be evenly divided by itself, in which case the quotient will be 1. ", f"Now {left[len(primef)-1]} can only be evenly divided by itself because it is a prime number, and the result is 1. ", f"At last {left[len(primef)-1]} is only divisible by {primef[len(primef)-1]} which is a prime number. So it can’t be factorized again. So, our factor tree is completed."]
#         content = content + wp_h4(h4_step) + \
#             wp_paragraph(random.choice(random_list)) + \
#             image_upload(divisionImages[len(divisionImages)-1])
# content = content + \
#     wp_paragraph(
#         "< strong > Note: We’ll have to repeat the process until the quotient becomes 1.< /strong >")
