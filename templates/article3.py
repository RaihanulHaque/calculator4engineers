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

    def wp_list(self, text):
        return f"<!-- wp:list {{\"ordered\":true}} --> {text} <!-- /wp:list -->"

    def wp_paragraph_center(self, text):
        return f"<!-- wp:paragraph {{\"align\":\"center\"}} --><p class = \"has-text-align-center\" >{text}</p> <!-- /wp:paragraph -->"

    def image_add_tree(self):
        locString = f"<!-- wp:image {{\"id\":452,\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
        locString += f"<figure class=\"wp-block-image size-full\"><img src=\"https://calculator4engineers.com/wp-content/uploads/2022/10/treefact.jpg\" alt=\"\" class=\"wp-image-452\"/></figure>"
        locString += "<!-- /wp:image -->"
        return locString

    def image_add_division(self):
        locString = f"<!-- wp:image {{\"id\":471,\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
        locString += f"<figure class=\"wp-block-image size-full\"><img src=\"https://calculator4engineers.com/wp-content/uploads/2022/10/unnamed.jpg\" alt=\"\" class=\"wp-image-471\"/></figure>"
        locString += "<!-- /wp:image -->"
        return locString

    def check_squared(self, n):
        root = sqrt(n)
        if int(root + 0.5) ** 2 == n:
            return f"Yes. The square root of {self.n} is an integer. So it is a square number."
        else:
            return f"No. The square root of 10365 isn’t an integer. So it isn’t a square number."

    def isPrime_or_Composite(self, n):
        primef, left, str_primef, multi_primef = self.primeFactors(n)
        if len(primef) > 1:
            return f"{self.n} is a composite number."
        else:
            return f"{self.n} is a prime number."

    def extraPrimeF(self, n):
        extracode = ""
        holdarr = []
        holdarrstr1 = ""
        holdarrstr2 = ""
        for x in range(1, int(sqrt(n))+1):
            if n % x == 0:
                extracode = extracode + \
                    self.wp_paragraph(f"{self.n} ÷ {x} = {int(n/x)}")
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

        return positive_factors, positive_non_prime_factors, negative_factors

    def sub(self, text):
        return f"<sub>{text}</sub>"

    def sup(self, text):
        return f"<sup>{text}</sup>"

    def strong(self, text):
        return f"<strong>{text}</strong>"

    def prepareTitle(self):
        title = f"Prime Factorization of {self.n}: Factor Tree, Division Methods"
        return title

    def prepareIntro(self):
        p1 = self.wp_paragraph(
            f"Prime factors of {self.n} are {self.str_primef}.")
        p2 = self.wp_paragraph(
            f"Here, if we multiply {self.str_primef}, we’ll get {self.n} as the product. So, {self.str_primef} are the factors of {self.n}. As {self.str_primef} are prime numbers, they are also the prime factors of {self.n}.")
        intro = p1 + p2

        intro += self.wp_table(
            f"""<tr>
                    <td>Prime Factors</td><td>{self.str_primef}</td>
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

        h = self.wp_h2("What is the Prime Factor?")
        post += h

        p = self.wp_paragraph("Factors are those integers which divide a number evenly and the remainder is 0. Or we can think the other way, if we multiply two numbers to get a product, then, those two numbers are the factors of that product. Factor is always an integer number. It can’t be a fraction. If the factors of a number are prime numbers, then they are called prime factors.")
        post += p

        c = self.wp_paragraph_center("105 = 3 x 5 x 7")
        post += c

        p = self.wp_paragraph(
            "Here, 105 is the product of multiplication of 3, 5, 7. All the multipliers are prime numbers. So, 3, 5, 7 are the prime factors of 105.")
        post += p

        h = self.wp_h2("What is Factorization?")
        post += h

        p = self.wp_paragraph(
            "The method of factorization involves finding all the numbers that divide a target number exactly. Using various methods of calculation, we can obtain all of those figures. Both the provided number and its divisors must be integers.")
        post += p

        h = self.wp_h2("What is Prime Factorization?")
        post += h

        p = self.wp_paragraph(
            "Prime factorization is the process of determining a group of prime numbers that, when multiplied, yield the specified integer.")
        post += p

        return post

    def prepareFormula(self):
        post = ""

        post += self.wp_h2("Formula of Prime Factor")
        post += self.wp_paragraph("Any composite number can be expressed as a product of powers of prime numbers. The process of expressing a number as a product of several prime numbers is known as prime factorization. Formula of prime factors:")
        post += self.wp_paragraph(
            "N = p<sub>f1</sub><sup>a1</sup> +&nbsp; p<sub>f2</sub><sup>a2</sup> +&nbsp; &nbsp; p<sub>f3</sub><sup>a3</sup> + ... ... +&nbsp; p<sub>fn</sub><sup>an</sup>")

        p = "N = Any integer number<br>"
        p += "p<sub>f1</sub>, p<sub>f2</sub>, p<sub>f3</sub>, p<sub>fn</sub> = Prime factors<br>"
        p += "a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>n</sub> = Orders of prime factors<br>"
        p = self.wp_paragraph(p)
        post += p
        return post

    def howtoCalculateList(self):
        post = ""
        post += self.wp_h2(
            f"How to Calculate the Prime Factors of {self.n}?")
        post += self.wp_paragraph(
            "Prime factors can be determined in several ways. Two of the most common methods are:")
        post += f"<!-- wp:list --><ul><li>Factor Tree Method. </li><li>Division Method.</li></ul><!-- /wp:list -->"
        return post

    def prepareFactorTree(self):
        post = ""
        post += self.wp_h3("Factor Tree Method")

        p1 = self.wp_paragraph(
            "In factor tree method, the given number and the factors of the given number will be connected via diagonals like this:")
        post += p1

        image = self.image_add_tree()
        post += image

        p2 = self.wp_paragraph(
            "Hence, it is called the Factor Tree Method. Here we’ll draw the given number as a root & factors as a tree. From the tree we’ll filter those factors which are prime numbers. We can do this step by step.")
        post += p2

        return post

    def prepareDivision(self):
        post = ""
        post += self.wp_h3("Division Method")

        p1 = self.wp_paragraph(
            "There is another popular method to find prime factors. It is called the division method. It's the simplest way to find factors. In this method, we need to divide the given number again & again.")

        image = self.image_add_division()

        p2 = self.wp_paragraph(
            "That’s why it is called the division method. Now we’ll walk through the process in steps:")

        post += p1 + image + p2
        return post

    def prepareExtra1(self):
        post = ""
        positive_factors, positive_non_prime_factors, negative_factors = self.extraPrimeF(
            self.n)

        closestprime = ""
        post += closestprime

        sec1 = self.wp_h2(f"Non-Prime Factors of {self.n}")
        sec1 += self.wp_paragraph(
            f"All the positive factors of {self.n} are {positive_factors}. So, the non-prime factors are {positive_non_prime_factors}")

        sec2 = self.wp_h2(f"Negative Factors of {self.n}")
        sec2 += self.wp_paragraph(
            f"The negative factors of {self.n} are {negative_factors}")

        post += sec1 + sec2

        return post

    def prepareExtra2(self):

        content = self.wp_h2("Facts About Factorization")
        list = "<ol>"
        list += "<li>Factors can’t be a fragment of a number.</li>"
        list += "<li>Given number must be an integer.</li>"
        list += "<li>Factors can be both negative & positive.</li>"
        list += "<li>1 is the factor of every natural number.</li>"
        list += "<li>A quadratic equation can also have factors.</li>"
        list += "<li>If we divide a given number, then the divisors & the quotient of the given number are also factors of it. Example:</li>"
        list += "</ol>"
        list = self.wp_list(list)
        content += list
        cp = self.wp_paragraph_center(
            "10365 ÷ 1 = 10365<br>10365 ÷ 3 = 3455<br>10365 ÷ 5 = 2073<br>10365 ÷ 15 = 691")
        content += cp
        content += self.wp_paragraph(
            "Here, both the divisors 1, 3, 5, 15 and the quotients 10365, 3455, 2073, 691 are the factors of 10365.")
        content += self.wp_h2("Application of Factorization in Daily Life")
        content += self.wp_paragraph("We use factors to arrange something in different ways. It helps us to divide something equally. In mathematics, it is used in various number related problems. Besides, it is used in comparing something, money exchange, understanding time etc. We can also factorize quadratic equations to simplify it.")
        return content

    def prepareFAQ(self):
        post = ""
        post += self.wp_h2("Frequently Asked Questions")

        post += self.wp_h3("1. Can Factors Be Negative?")
        post += self.wp_paragraph("Yes. Factors can be negative too. Like the factors of 10 are 1, 2, 5, 10, -1, -2, -5, -10. Because if we multiply -10 with -1, we’ll get 10. So, -10 & -1 are the factors of 10. But most of the time we use positive factors only.")

        post += self.wp_h3(f"2. Is {self.n} a Square Number?")
        post += self.wp_paragraph(self.check_squared(self.n))

        post += self.wp_h3(f"3. Square of {self.n}?")
        post += self.wp_paragraph(f"Square of {self.n} is {self.n*self.n}.")

        post += self.wp_h3(f"4. Root of {self.n}?")
        post += self.wp_paragraph(f"Root of {self.n} is {sqrt(self.n)}")

        post += self.wp_h3(
            f"5. Is {self.n} a Composite Number or a Prime Number?")
        post += self.wp_paragraph(self.isPrime_or_Composite(self.n))

        post += self.wp_h3(f"6. How Many Factors Does a Prime Number Have?")
        post += self.wp_paragraph(
            "A Prime number has only 2. They are 1 & the number itself.")

        post += self.wp_h3("7. What is a Composite Number?")
        post += self.wp_paragraph(
            "If a positive integer number has more than two factors, it can be called a composite number.")

        return post


if __name__ == "__main__":

    post = Post(1003)
    postHtml = ""
    # postHtml = "<html>"
    # postHtml += submitWP.title
    postHtml += post.intro
    postHtml += post.theory
    postHtml += post.formula
    postHtml += post.howtocalculatelist
    postHtml += post.factorTree
    postHtml += post.division
    postHtml += post.extra1
    postHtml += post.extra2
    postHtml += post.FAQ

    with open("view.html", "w") as htmlFile:
        htmlFile.write(postHtml)
    print(submitWP.submit(post.title, content=postHtml))
