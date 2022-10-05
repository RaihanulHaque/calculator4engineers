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
        title = f"Prime Factorization of {self.n}: Factor Tree, Division Methods"
        return title

    def prepareIntro(self):
        p1 = self.wp_paragraph(
            f"Prime factors of {self.n} are {self.str_primef}.")
        p2 = self.wp_paragraph(
            f"Here, if we multiply {self.str_primef}, we’ll get {self.n} as the product. So, {self.str_primef} are the factors of {self.n}. As {self.str_primef} are prime numbers, they are also the prime factors of {self.n}.")
        intro = p1 + p2
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

        h = self.wp_h2("Formula of Prime Factor")
        post += h

        p = self.wp_paragraph(
            "Any composite number can be expressed as a product of powers of prime numbers. The process of expressing a number as a product of several prime numbers is known as prime factorization. Formula of prime factors:")
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
            f"How to Calculate the Prime Factors of {self.n}?")
        post += self.wp_paragraph(
            "Prime factors can be determined in several ways. Two of the most common methods are:")
        post += f"<!-- wp:list --><ul><li>Factor Tree Method. </li><li>Division Method.</li></ul><!-- /wp:list -->"
        return post

    def factorTree(self):
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


if __name__ == "__main__":

    post = Post(48)
    postHtml = ""
    # postHtml = "<html>"
    # postHtml += submitWP.title
    postHtml += post.intro
    postHtml += post.theory
    postHtml += post.howtocalculatelist
    postHtml += post.factorTree
    # postHtml += "</html>"

    with open("view.html", "w") as htmlFile:
        htmlFile.write(postHtml)
    print(submitWP.submit(post.title, content=postHtml))
