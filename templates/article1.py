import random
from math import floor, sqrt
import submitWP


class Post:
    def __init__(self, n):
        self.n = n
        self.primef, self.left, self.str_primef, self.multi_primef = self.primeFactors(
            n)
        self.title = self.prepareTitle()
        self.intro = self.prepareIntro()
        self.theory = self.prepareTheory()
        self.formula = self.prepareFormula()
        self.howtocalculatelist = self.howtoCalculateList()
        self.factorTree = self.prepareFactorTree()
        self.division = self.prepareDivision()
        self.extra1 = self.prepareExtra1()
        self.extra2 = self.prepareExtra2()
        self.FAQ = self.prepareFAQ()

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
                str_primef = str_primef+f"{c}, "
                multi_primef = multi_primef + f"{c} x "
                # expo_primef = expo_primef + f"{c}<sup>1</sup> x "
                n = n / c
            else:
                c = c + 1
        left.append(1)
        return primef, left, str_primef[:-2], multi_primef[:-2]

    def unique_primef(self, n):
        unique_arr = [*set(self.primef)]
        str_unique = ""
        for x in range(0, len(unique_arr) - 1):
            str_unique += f"{unique_arr[x]}, "
        str_unique = f"{str_unique[:-2]} and {unique_arr[len(unique_arr)-1]}"

        return str_unique

    def exponential(self, array):
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

    def nearestPrime(self, n):
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

    def wp_h2(self, text):
        return f"<!-- wp:heading {{\"level\":2}} --><h2>{text}</h2><!-- /wp:heading -->"

    def wp_h3(self, text):
        return f"<!-- wp:heading {{\"level\":3}} --><h3>{text}</h3><!-- /wp:heading -->"

    def wp_paragraph(self, text):
        return f"<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->"

    def wp_table(self, text):
        table = f"""<!-- wp:table {{\"hasFixedLayout\":true,\"className\":\" is -style-stripes prime-factorization-table\"}} -->
        <figure class=\"wp-block-table is-style-stripes prime-factorization-table\">
        <table class=\"has-fixed-layout\">
            <tbody>
                {text}
            </tbody>
        </table>
        <figcaption>Prime Factorization of {self.n}</figcaption>
        </figure>
        <!-- /wp:table -->"""
        return table

    def wp_paragraph_center(self, text):
        return f"<!-- wp:paragraph {{\"align\":\"center\"}} --><p class = \"has-text-align-center\" >{text}</p> <!-- /wp:paragraph -->"

    def image_add_tree(self):
        locString = f"<!-- wp:image {{\"id\":452,\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
        locString += f"<figure class=\"wp-block-image size-full\"><img src=\"https://calculator4engineers.com/wp-content/uploads/2022/10/factor-tree-method.jpg\" alt=\"\" class=\"wp-image-452\"/></figure>"
        locString += "<!-- /wp:image -->"
        return locString

    def image_add_division(self):
        locString = f"<!-- wp:image {{\"id\":471,\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
        locString += f"<figure class=\"wp-block-image size-full\"><img src=\"https://calculator4engineers.com/wp-content/uploads/2022/10/division-method.jpg\" alt=\"\" class=\"wp-image-471\"/></figure>"
        locString += "<!-- /wp:image -->"
        return locString

    def check_squared(self, n):
        root = sqrt(n)
        if int(root + 0.5) ** 2 == n:
            return f"Yes. The square root of {self.n} is an integer. So it is a square number."
        else:
            return f"No. The square root of 10365 isn’t an integer. So it isn’t a square number."

    def isPrime_or_Composite(self, n):
        # primef, left, str_primef, multi_primef = self.primeFactors(n)
        if len(self.primef) > 1:
            return f"{self.n} is a composite number."
        else:
            return f"{self.n} is a prime number."

    def extraPrimeF(self, n):
        division_code = ""
        multiply_code = ""
        holdarr = []
        holdarrstr1 = ""
        holdarrstr2 = ""

        for x in range(1, int(sqrt(n))+1):
            if n % x == 0:
                division_code += self.wp_paragraph(
                    f"{self.n} ÷ {x} = {int(n/x)}")
                multiply_code += self.wp_paragraph(f"-{int(n/x)} x -{x} = {n}")
                holdarr.append(x)
                holdarr.append(int(n/x))

        holdarr.sort()

        for y in range(0, len(holdarr)):
            holdarrstr1 = holdarrstr1 + f"{holdarr[y]}, "
            holdarrstr2 = holdarrstr2 + f"-{holdarr[y]}, "
        nonPrimefact = ""

        for x in range(0, len(self.primef)):
            if self.primef[x] in holdarr:
                holdarr.remove(self.primef[x])

        for x in range(0, len(holdarr)):
            nonPrimefact = nonPrimefact + f"{holdarr[x]}, "

        positive_factors = holdarrstr1[:-2]
        positive_non_prime_factors = nonPrimefact[:-2]
        negative_factors = holdarrstr2[:-2]

        return positive_factors, positive_non_prime_factors, negative_factors, division_code, multiply_code

    def sub(self, text):
        return f"<sub>{text}</sub>"

    def sup(self, text):
        return f"<sup>{text}</sup>"

    def strong(self, text):
        return f"<strong>{text}</strong>"

    def prepareTitle(self):
        title = f"Prime Factorization of {self.n}: Solved with Images"
        return title

    def prepareIntro(self):
        p1 = self.wp_paragraph(
            f"{self.multi_primef}= {self.n}. So, the <strong>prime factors</strong> of {self.n} are {self.unique_primef(self.n)}.")
        p2 = self.wp_paragraph(
            f"{self.n} can be written as the product of {self.str_primef}. So, {self.str_primef} are the <strong>factors</strong> of {self.n}. They are <strong>prime numbers</strong> as well. Thus, {self.unique_primef(self.n)} become the <strong>prime factors</strong> of {self.n}.")
        intro = p1 + p2

        intro += self.wp_table(
            f"""<tr>
                    <td>Prime Factors</td><td>{self.unique_primef(self.n)}</td>
                </tr>
                <tr>
                    <td>Product of Prime Factor</td><td>{self.multi_primef}</td>
                </tr>
                <tr>
                    <td>Exponential Form</td><td>{self.exponential(self.primef)}</td>
                </tr>
                <tr>
                    <td>Total Number of Factors</td><td>{len(self.primef)}</td>
                </tr>
                <tr>
                    <td>Largest Prime Factor</td><td>{max(self.primef)}</td>
                </tr>
                <tr>
                    <td>Smallest Prime Factor</td><td>{min(self.primef)}</td>
                </tr>
                <tr>
                    <td>Closest Prime Numbers</td><td>{self.nearestPrime(self.n)}</td>
                </tr>""")
        return intro

    def prepareTheory(self):
        post = ""

        h = self.wp_h2("Prime Factors by Definition")
        post += h

        p = self.wp_paragraph("The term factors indicate those integers which divide a number in such a way that the remainder becomes 0. Contrarily, the multipliers of a product can be depicted as the factors of that product. But remember, a factor mustn’t be a fraction number. So, we can use only the integers as the multipliers. If the factors of a number are prime numbers, then they are called prime factors.")
        post += p

        c = self.wp_paragraph_center("105 = 3 x 5 x 7")
        post += c

        p = self.wp_paragraph(
            "Here, 105 is the product of multiplication of 3, 5, 7. All the multipliers are prime numbers. So, 3, 5, 7 are the prime factors of 105.")
        post += p

        h = self.wp_h2("What is Factorization?")
        post += h

        p = self.wp_paragraph(
            "The process of determining factors is known as factorization.")
        post += p

        h = self.wp_h2("What is Prime Factorization?")
        post += h

        p = self.wp_paragraph(
            "Prime factorization is a type of factorization where we determine only those factors which are prime numbers.")
        post += p

        return post

    def prepareFormula(self):
        post = ""

        post += self.wp_h2("Formula of Prime Factor")
        post += self.wp_paragraph("It is possible to write any composite number as the product of powers of prime numbers. When a number is written as the product of multiple prime numbers, the process is called prime factorization. Mathematical expression for prime factors:")
        post += self.wp_paragraph_center(
            "N = p<sub>f1</sub><sup>a1</sup> +&nbsp; p<sub>f2</sub><sup>a2</sup> +&nbsp; &nbsp; p<sub>f3</sub><sup>a3</sup> + ...... +&nbsp; p<sub>fn</sub><sup>an</sup>")

        p = "N = Any integer number<br>"
        p += "p<sub>f1</sub>, p<sub>f2</sub>, p<sub>f3</sub>, p<sub>fn</sub> = Prime factors<br>"
        p += "a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>n</sub> = Orders of prime factors<br>"
        p = self.wp_paragraph(p)
        post += p
        return post

    def howtoCalculateList(self):
        post = ""
        post += self.wp_h2(f"How to Calculate the Prime Factors of {self.n}?")
        post += self.wp_paragraph(
            "Prime factors can be determined in several ways. Two of the most common methods are:")
        post += f"<!-- wp:list --><ul><li>Factor tree method.</li><li>Division method.</li></ul><!-- /wp:list -->"
        return post

    def prepareFactorTree(self):
        post = ""
        post += self.wp_h3("Factor Tree Method")

        p1 = self.wp_paragraph(
            "Here, the target number serves as the tree's root, while the factors are its branches. For this reason, we refer to it as the Factor Tree Approach.")

        image = self.image_add_tree()

        p2 = self.wp_paragraph("In this case, we'll represent the supplied number as the root of a tree and its factors as their respective branches. We'll use diagonals to graphically represent the relationship between the two variables and the tree structures. We'll extract just prime factors from the tree. By breaking it down into manageable chunks, we can accomplish it.")

        post += p1 + image + p2
        return post

    def prepareDivision(self):
        post = ""
        post += self.wp_h3("Division Method")

        p1 = self.wp_paragraph(
            "To find prime factors, you can also use another well-known technique. The process is known as division. Finding factors in this manner is the least complicated option.This approach requires repeated division by the specified number.")

        image = self.image_add_division()

        p2 = self.wp_paragraph(
            "That's why it's referred to as a \"division method.\" Here's how it works, step by step:")

        post += p1 + image + p2
        return post

    def prepareExtra1(self):
        post = ""
        positive_factors, positive_non_prime_factors, negative_factors, division_code, multiply_code = self.extraPrimeF(
            self.n)

        # closestprime = ""
        # post += closestprime

        sec1 = self.wp_h2(f"Non-Prime Factors of {self.n}")
        sec1 += self.wp_paragraph(
            f"All the positive factors of {self.n} are {positive_factors}. So, the non-prime factors are {positive_non_prime_factors}")

        sec2 = self.wp_h2(f"Negative Factors of {self.n}")
        sec2 += self.wp_paragraph(
            f"The negative factors of {self.n} are {negative_factors}")

        sec3 = self.wp_h2(f"How to Determine All the Factors of {self.n}?")
        sec3 += self.wp_paragraph(
            f"To determine all the factors of {self.n}, we have to find every divisor that divides {self.n} exactly. After finding that, we should express this like this:")
        sec3 += division_code
        sec3 += self.wp_paragraph(
            f"Here every divisor & quotient are the factors of {self.n}. <br><br> So, the positive factors of 10365 are: {positive_factors}.")
        sec3 += self.wp_paragraph(f"We can also express this like:")
        sec3 += multiply_code
        sec3 += self.wp_paragraph(
            f"So the negative factors are: {negative_factors}.<br><br>Remember, a negative factor must multiply with another negative factor only to get our given number.")

        post += sec1 + sec2 + sec3

        return post

    def prepareExtra2(self):
        post = ""

        sec1 = self.wp_h2(f"Facts of Factorization")
        sec1 += f"""<!-- wp:list {{\"ordered\":true}} -->
        <ol>
            <li>No fractional parts of numbers can be used as factors.</li>
            <li> The number you enter must be a whole number.</li>
            <li>Factors can be both negative & positive.</li>
            <li>Each and every natural number has 1 as a factor.</li>
            <li>An equation with quadratic terms can also be factored.</li>
        </ol>
        <!-- /wp:list -->"""

        sec2 = self.wp_h2(f"Use of Factors")
        sec2 += self.wp_paragraph(f"Factors allow us to put things in various configurations. It's useful for making fair divisions. It has several applications in mathematics involving numbers. The ability to do so is also helpful when making comparisons, exchanging money, telling time, etc. Quadratic equations can also be factored to make solving them easier.")

        post = sec1 + sec2

        return post

    def prepareFAQ(self):
        post = ""
        post += self.wp_h2("Frequently Asked Questions")

        post += self.wp_h3("1. Can Factors Be Negative?")
        post += self.wp_paragraph("Yes. Factors can be negative too. Like the factors of 10 are 1, 2, 5, 10, -1, -2, -5, -10. Because if we multiply -10 with -1, we’ll get 10. So, -10 & -1 are the factors of 10. But most of the time we use positive factors only.")

        post += self.wp_h3(f"2. Is {self.n} a Square Number?")
        post += self.wp_paragraph(self.check_squared(self.n))

        post += self.wp_h3(f"3. What Is the Square of {self.n}?")
        post += self.wp_paragraph(f"Square of {self.n} is {self.n*self.n}.")

        post += self.wp_h3(f"4. What Is the Root of {self.n}?")
        post += self.wp_paragraph(f"Root of {self.n} is {sqrt(self.n)}")

        post += self.wp_h3(
            f"5. Is {self.n} a Composite Number or a Prime Number?")
        post += self.wp_paragraph(self.isPrime_or_Composite(self.n))

        post += self.wp_h3(f"6. How Many Factors Does a Prime Number Have?")
        post += self.wp_paragraph(
            "A Prime number has only 2 factors. They are 1 & the number itself.")

        post += self.wp_h3("7. What is a Composite Number?")
        post += self.wp_paragraph(
            "If a positive integer number has more than two factors, it can be called a composite number.")

        post += self.wp_h3("8. What are the factors of a prime number?")
        post += self.wp_paragraph("They are 1 & the number itself.")

        return post


if __name__ == "__main__":

    post = Post(56)
    postHtml = ""
    # postHtml = "<html>"
    # postHtml += submitWP.title
    postHtml += post.intro
    postHtml += post.theory
    postHtml += post.howtocalculatelist
    postHtml += post.factorTree
    postHtml += post.extra1
    postHtml += post.extra2
    # postHtml += "</html>"

    with open("view.html", "w") as htmlFile:
        htmlFile.write(postHtml)
    print(submitWP.submit(post.title, content=postHtml))
