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
        self.howtocalculatelist = self.howtoCalculateList()
        self.factorTree = self.factorTree()

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

    def wp_paragraph_center(self, text):
        return f"<!-- wp:paragraph {{\"align\":\"center\"}} --><p class = \"has-text-align-center\" >{text}</p> <!-- /wp: paragraph -->"

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

    def sub(self, text):
        return f"<sub>{text}</sub>"

    def sup(self, text):
        return f"<sup>{text}</sup>"

    def strong(self, text):
        return f"<strong>{text}</strong>"

    def prepareTitle(self):
        title = f"Prime Factorization of {self.n}: Step by Step Calculation"
        return title

    def prepareIntro(self):
        p1 = self.wp_paragraph(
            f"{self.str_primef} are the prime factors of {self.n}.")
        p2 = self.wp_paragraph(
            f"{self.str_primef} are the prime numbers and you'll get {self.n} if you multiply {self.str_primef}. So {self.str_primef} are the prime factors of {self.n}.")
        intro = p1 + p2
        return intro

    def prepareTheory(self):
        post = ""

        h = self.wp_h2("Introduction to Prime Factors")
        post += h

        p = self.wp_paragraph("Before learning the methods of calculating prime factors, we should get familiar with the term prime factors. What are prime factors? And why are they called prime factors? Prime factors are those integers which can express a given number as a form of their multiplication. In other words, if we multiply two prime numbers, we’ll get another number and those previous numbers are the prime factors of the later one. We’ll be more clear with an example :")
        post += p

        c = self.wp_paragraph_center("105 = 3 x 5 x 7")
        post += c

        p = self.wp_paragraph(
            "Here, the multiplication of the prime numbers 3, 5 & 7 form 365. So, 3, 5 & 7 are the prime factors of 365. From the above example, we get to know another important thing: our given number is always evenly divisible by the prime factors. As we see, 365 is evenly divisible by 3, 5 & 7. They’re being called prime factors because they are prime numbers. If they weren't prime numbers, they would’ve been called only factors.")
        post += p

        h = self.wp_h2("Definition of Factorization")
        post += h

        p = self.wp_paragraph(
            "Factorization is the process to determine all the numbers that exactly divide a given number. We can find all those numbers through different calculation methods. But remember, the given number as well as the divisors must be integer numbers.")
        post += p

        h = self.wp_h2("Definition of Prime Factorization")
        post += h

        p = self.wp_paragraph(
            "Prime factorization is also a kind of factorization but the only difference is the divisors are prime numbers in this case.")
        post += p

        h = self.wp_h2("Prime Factors’ Formula")
        post += h

        p = self.wp_paragraph("A prime factor must be a prime number as well as a factor of the given number. Basically, prime factors can be found by decomposing our given number. It can be expressed as a product of prime numbers with orders. In general, we represent our given number as a product of prime numbers with their orders. These prime numbers are certainly the prime factors of the given number.")
        post += p

        c = self.wp_paragraph(
            "N = p<sub>f1</sub><sup>a1</sup> +&nbsp; p<sub>f2</sub><sup>a2</sup> +&nbsp; &nbsp; p<sub>f3</sub><sup>a3</sup> + ... ... +&nbsp; p<sub>fn</sub><sup>an</sup>")
        post += c

        p = "N = Any integer number<br>"
        p += "p<sub>f1</sub>, p<sub>f2</sub>, p<sub>f3</sub>, p<sub>fn</sub> = Prime factors<br>"
        p += "a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>n</sub> = Orders of prime factors<br>"
        p = self.wp_paragraph(p)
        post += p

        return post

    def howtoCalculateList(self):
        post = ""
        post += self.wp_h2(
            f"Methods of Calculating Prime Factors of {n}?")
        post += self.wp_paragraph(
            "The process of finding prime factors of a number is called prime factorization. We can determine the prime factors of 10365 in multiple ways. But here, we’ll talk about the popular methods only.")
        post += f"<!-- wp:list --><ul><li>Division Method & </li><li>Factor Tree Method.</li></ul><!-- /wp:list -->"
        return post

    def factorTree(self):
        post = ""
        post += self.wp_h3("Factor Tree Method")

        p1 = self.wp_paragraph(
            "Factor tree method, mainly a diagram based method. The reason behind this name is because  the diagram we found in the factor tree method looks like a tree. The given number is the root and prime factors are the branches of the tree. In this method, the prime factors sit at the top of every branch.")
        post += p1

        # image = self.image_add_tree()
        # post += image

        # p2 = self.wp_paragraph("In this case, we'll represent the supplied number as the root of a tree and its factors as their respective branches. We'll use diagonals to graphically represent the relationship between the two variables and the tree structures. We'll extract just prime factors from the tree. By breaking it down into manageable chunks, we can accomplish it.")
        # post += p2

        return post


if __name__ == "__main__":

    post = Post(48)
    postHtml = ""
    # postHtml = "<html>"
    # postHtml += submitWP.title
    postHtml += post.intro
    postHtml += post.theory
    # postHtml += "</html>"

    with open("view.html", "w") as htmlFile:
        htmlFile.write(postHtml)
    print(submitWP.submit(post.title, content=postHtml))
