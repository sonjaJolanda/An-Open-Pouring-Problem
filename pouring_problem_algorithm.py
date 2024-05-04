import math

class pouring_problem: 
    a = 0
    b = 0
    c = 0
    step_counter = 0
    def __init__(self, a, b, c):
        if (a < 0 or b < 0 or c < 0):
            raise ValueError("Pitchers must have positive capacity")
        if (a == 0 or b == 0 or c == 0):
            raise ValueError("The problem is already sloved, one of the pitchers is 0")
        
        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print("[%(a)s, %(b)s, %(c)s]" % {'a' : self.a, 'b': self.b, 'c': self.c})

    def sort (self):
        print("SORTING... ", end="")
        sorted_numbers = sorted([self.a, self.b, self.c])
        self.a = sorted_numbers[0]
        self.b = sorted_numbers[1]
        self.c = sorted_numbers[2]  
        self.print()

    def case_1(self, p_bin):
        print("\tCASE 1:")
        k = len(p_bin)
        old_a = self.a
        for i in range(k):
            self.step_counter += 1
            print("\t\tStep %(step_nr)s: p_i = %(p_i)s ----> " % {'step_nr': self.step_counter, 'p_i' : p_bin[-(i+1)]}, end="")
            if p_bin[-(i+1)] == 1:
                self.b = self.b - ((2**i)*old_a)
            if p_bin[-(i+1)] == 0: 
                self.c = self.c - ((2**i)*old_a)
            self.a = self.a + ((2**i)*old_a)
            self.print()

    def case_2(self, q_bin):
        print("\tCASE 2:")
        l = len(q_bin)
        old_a = self.a
        for i in range(l):
            self.step_counter += 1
            print("\t\tStep %(step_nr)s: q_i = %(q_i)s ----> " % {'step_nr': self.step_counter, 'q_i' : q_bin[-(i+1)]}, end="")
            if q_bin[-(i+1)] == 1:
                self.b = self.b - ((2**i)*old_a)
            if q_bin[-(i+1)] == 0: 
                self.c = self.c - ((2**i)*old_a)
            self.b = self.b + ((2**i)*old_a)
            self.print()
    
    def pouring(self):
        self.sort()
        print("START POURING:")
        round_counter = 0
        while (self.a >= 1): # rounds
            round_counter += 1
            print("ROUND %(round_counter)s: " % {'round_counter' : round_counter}, end="")
            self.print()
            p = math.floor(self.b/self.a)
            q = math.ceil(self.b/self.a)

            binary_p_string = bin(p)[2:]  # Convert the integer p to binary string and remove '0b' prefix
            p_bin = [int(bit) for bit in binary_p_string]

            binary_q_string = bin(q)[2:]  # Convert the integer q to binary string and remove '0b' prefix
            q_bin = [int(bit) for bit in binary_q_string]

            print("\tp: %(p)s (%(p_bin)s), q: %(q)s (%(q_bin)s)" % {'p' : p, 'p_bin': binary_p_string, 'q': q, 'q_bin': binary_q_string})
            
            if ((self.b - (p*self.a)) <= (self.a/2)):
                    self.case_1(p_bin)
            elif ((q-self.a) - self.b) < (self.a/2):
                    self.case_2(q_bin)
            print("\t", end="")
            self.sort()
        print("DONE in %(rounds)s rounds and %(steps)s steps!" % {'rounds': round_counter, 'steps': self.step_counter})



problem = pouring_problem(42, 19, 2)
problem.pouring()
