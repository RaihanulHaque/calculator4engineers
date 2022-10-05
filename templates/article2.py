import random
from math import floor, sqrt


class Post:
    def __init__(self, n):
        self.n = n
        self.primef, self.left, self.str_primef, self.multi_primef = self.primeFactors(
            n)
        self.titles = []
        self.title = self.prepareTitle()
        self.intros = []
        self.intro = self.prepareIntro()
        self.theories = []
        # self.theory = self.prepareTheory()

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
        # self.titles.append(
        #     f"Prime Factorization of {self.n}: Solved with Images"
        # )
        self.titles.append(
            f"Prime Factorization of {self.n}: Step by Step Calculation")
        # self.titles.append(
        #     f"Prime Factorization of {self.n}: Factor Tree, Division Methods")
        return random.choice(self.titles)

    def prepareIntro(self):
        # l1 = f"""{self.str_primef} are the prime factors of {self.n}."""
        # l2 = f"""{self.str_primef} are prime numbers and you’ll get {self.n} if you multiply {self.str_primef}. So, {self.str_primef} are the prime factors of {self.n}."""
        # self.intros.append(wp_paragraph(l1) + wp_paragraph(l2))

        self.intros.append(
            f"""Prime factors of {self.n} are {self.str_primef}.
                Here, if we multiply {self.str_primef}, we’ll get {self.n} as the product. So, {self.str_primef} are the factors of {self.n}. As {self.str_primef} are prime numbers, they are also the prime factors of {self.n}."""
        )
        # self.intros.append(
        #     f"""{self.multi_primef}= {self.n}. So, the prime factors of {self.n} are {self.str_primef}. {self.n} can be written as the product of {self.str_primef}. So, {self.str_primef} are the factors of {self.n}. They are prime numbers as well. Thus, {self.str_primef} become the prime factors of {self.n}."""
        # )
        # self.intros[-1] += self.wp_table(
        #     f"""<tr>
        #             <td>Prime Factors</td><td>{self.str_primef}</td>
        #         </tr>
        #         <tr>
        #             <td>Product of Prime Factor</td><td>{self.multi_primef}</td>
        #         </tr>
        #         <tr>
        #             <td>Exponential Form</td><td>{self.exponential(self.primef)}</td>
        #         </tr>
        #         <tr>
        #             <td>Total Number of Factors</td><td>{len(self.primef)}</td>
        #         </tr>
        #         <tr>
        #             <td>Largest Prime Factor</td><td>{max(self.primef)}</td>
        #         </tr>
        #         <tr>
        #             <td>Smallest Prime Factor</td><td>{min(self.primef)}</td>
        #         </tr>
        #         <tr>
        #             <td>Closest Prime Numbers</td><td>{self.nearestPrime(self.n)}</td>
        #         </tr>""")

        return random.choice(self.intros)

    # def prepareTheory(self):
    #     self.theories.append(
    #         f"""Prime Factors by Definition
    #             The term factors indicate those integers which divide a number in such a way that the remainder becomes 0. Contrarily, the multipliers of a product can be depicted as the factors of that product. But remember, a factor mustn’t be a fraction number. So, we can use only the integers as the multipliers. If the factors of a number are prime numbers, then they are called prime factors.
    #             105 = 3*5*7
    #             Here, 105 is the product of multiplication of 3, 5, 7. All the multipliers are prime numbers. So, 3, 5, 7 are the prime factors of 105.
    #             What is Factorization?
    #             The process of determining factors is known as factorization.
    #             What is Prime Factorization?
    #             Prime factorization is a type of factorization where we determine only those factors which are prime numbers.
    #             Formula of Prime Factor
    #             It is possible to write any composite number as the product of powers of prime numbers. When a number is written as the product of multiple prime numbers, the process is called prime factorization. Mathematical expression for prime factors:
    #             N = pf1a1 × pf2a2 ×  pf3a3 × ... ... × pfnan
    #             N = Any integer number
    #             pf1, pf2, pf3, pfn = Prime factors
    #             a1 ,a2, a3, an = Orders of prime factors
    #             """)

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


# post = Post(48)
# print(post.intro)
