import math


class pouring_problem:
    a = 0
    b = 0
    c = 0
    step_counter = 0
    output_file = None

    def __init__(self, a, b, c, output_file):
        file = self.output_file = output_file

        if a < 0 or b < 0 or c < 0:
            raise ValueError("Pitchers must have positive capacity")
        if a == 0 or b == 0 or c == 0:
            raise ValueError("The problem is already sloved, one of the pitchers is 0")

        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print(
            "[%(a)s, %(b)s, %(c)s]" % {"a": self.a, "b": self.b, "c": self.c},
            file=self.output_file,
        )

    def sort(self):
        print("SORTING... ", file=self.output_file, end="")
        sorted_numbers = sorted([self.a, self.b, self.c])
        self.a = sorted_numbers[0]
        self.b = sorted_numbers[1]
        self.c = sorted_numbers[2]
        self.print()

    def case_1(self, p_bin):
        k = len(p_bin)
        print("\tCASE 1 (k=%(k)s):" % {"k": k}, file=self.output_file)
        old_a = self.a
        for i in range(k):
            self.step_counter += 1
            print(
                "\t\tStep %(step_nr)s: p_i = %(p_i)s ----> "
                % {"step_nr": self.step_counter, "p_i": p_bin[-(i + 1)]},
                file=self.output_file,
                end="",
            )
            if p_bin[-(i + 1)] == 1:
                self.b = self.b - ((2**i) * old_a)
            if p_bin[-(i + 1)] == 0:
                self.c = self.c - ((2**i) * old_a)
            self.a = self.a + ((2**i) * old_a)
            self.print()

    def case_2(self, q_bin):
        l = len(q_bin)
        print("\tCASE 2 (l=%(l)s):" % {"l": l}, file=self.output_file)
        old_a = self.a
        for i in range(l - 1):
            self.step_counter += 1
            print(
                "\t\tStep %(step_nr)s: q_i = %(q_i)s ----> "
                % {"step_nr": self.step_counter, "q_i": q_bin[-(i + 1)]},
                file=self.output_file,
                end="",
            )
            if q_bin[-(i + 1)] == 1:
                self.b = self.b - ((2**i) * old_a)
            if q_bin[-(i + 1)] == 0:
                self.c = self.c - ((2**i) * old_a)
            self.a = self.a + ((2**i) * old_a)
            self.print()
        # last step does something else
        self.step_counter += 1
        print(
            "\t\tStep %(step_nr)s: ----> " % {"step_nr": self.step_counter},
            file=self.output_file,
            end="",
        )
        self.a = self.a - self.b
        self.b = self.b * 2
        self.print()

    def pouring(self):
        self.sort()
        print("START POURING:", file=self.output_file)
        round_counter = 0
        while self.a >= 1:  # rounds
            round_counter += 1
            print(
                "ROUND %(round_counter)s: " % {"round_counter": round_counter},
                file=self.output_file,
                end="",
            )
            self.print()
            p = math.floor(self.b / self.a)
            q = math.ceil(self.b / self.a)

            binary_p_string = bin(p)[
                2:
            ]  # Convert the integer p to binary string and remove '0b' prefix
            p_bin = [int(bit) for bit in binary_p_string]

            binary_q_string = bin(q)[
                2:
            ]  # Convert the integer q to binary string and remove '0b' prefix
            q_bin = [int(bit) for bit in binary_q_string]

            print(
                "\tp:%(p)s (%(p_bin)s), q:%(q)s (%(q_bin)s)"
                % {"p": p, "p_bin": binary_p_string, "q": q, "q_bin": binary_q_string},
                file=self.output_file,
            )

            if (self.b - (p * self.a)) <= (self.a / 2):
                print(
                    "\tb:%(b)s, p:%(p)s, a:%(a)s" % {"b": self.b, "p": p, "a": self.a},
                    file=self.output_file,
                )
                self.case_1(p_bin)
            elif ((q * self.a) - self.b) < (self.a / 2):
                print(
                    "\tb:%(b)s, q:%(q)s, a:%(a)s" % {"b": self.b, "q": q, "a": self.a},
                    file=self.output_file,
                )
                self.case_2(q_bin)
            print("\t", file=self.output_file, end="")
            self.sort()
        print(
            "DONE in %(rounds)s rounds and %(steps)s steps!"
            % {"rounds": round_counter, "steps": self.step_counter},
            file=self.output_file,
        )
