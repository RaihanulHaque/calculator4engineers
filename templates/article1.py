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

    def prepareTitle(self):
        title = f"Prime Factorization of {self.n}: Solved with Images"
        return title

    def prepareIntro(self):
        p1 = self.wp_paragraph(
            f"{self.multi_primef}= {self.n}. So, the prime factors of {self.n} are {self.str_primef}.")
        p2 = self.wp_paragraph(
            f"{self.n} can be written as the product of {self.str_primef}. So, {self.str_primef} are the factors of {self.n}. They are prime numbers as well. Thus, {self.str_primef} become the prime factors of {self.n}.")
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

        h = self.wp_h2("Formula of Prime Factor")
        post += h

        p = self.wp_paragraph("It is possible to write any composite number as the product of powers of prime numbers. When a number is written as the product of multiple prime numbers, the process is called prime factorization. Mathematical expression for prime factors:")
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

    def wp_h2(self, text):
        return f"<!-- wp:heading {{\"level\":2}} --><h2>{text}</h2><!-- /wp:heading -->"

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

    def sub(self, text):
        return f"<sub>{text}</sub>"

    def sup(self, text):
        return f"<sup>{text}</sup>"


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
