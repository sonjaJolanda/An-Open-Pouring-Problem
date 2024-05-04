from pouring_problem_algorithm import pouring_problem


def apply(N, n, a, b, c, output_file):
    print(
        "The Problem is (%(a)s, %(b)s, %(c)s) and N(%(N)s) and n=%(n)s"
        % {"a": a, "b": b, "c": c, "N": N, "n": n},
        file=output_file,
    )
    problem = pouring_problem(a, b, c, file)
    problem.pouring()
    print(
        "-----------------------------------------------\n-----------------------------------------------",
        file=output_file,
    )


with open("output.txt", "w") as file:
    # N(1) and n=3
    apply(1, 3, 1, 1, 1, file)
    # N(2) and n=6
    apply(2, 6, 1, 2, 3, file)
    # N(3) and n=11
    apply(3, 11, 1, 4, 6, file)
    # N(4) and n=15
    apply(4, 15, 4, 5, 6, file)
    apply(4, 15, 3, 4, 8, file)
    apply(4, 15, 2, 5, 8, file)
    # N(5) and n=23
    apply(5, 23, 3, 8, 12, file)
    # N(6) and n=27
    apply(6, 27, 5, 9, 13, file)
    # N(7) and n=45
    apply(7, 45, 4, 15, 26, file)
    # N(8) and n=81
    apply(8, 81, 8, 27, 46, file)
    # N(9) and n=105
    apply(9, 105, 27, 35, 43, file)
    apply(9, 105, 8, 35, 62, file)
    apply(9, 105, 8, 27, 70, file)
    # N(10) and n=195
    apply(10, 195, 57, 65, 73, file)
    apply(10, 195, 8, 78, 109, file)
    apply(10, 195, 4, 78, 112, file)
    apply(10, 195, 8, 73, 114, file)
    apply(10, 195, 8, 65, 122, file)
    apply(10, 195, 4, 66, 125, file)
    apply(10, 195, 8, 57, 130, file)
    apply(10, 195, 4, 33, 158, file)
    # N(11) and n=329
    apply(11, 329, 4, 130, 195, file)
    # N(12) and n=597
    apply(12, 597, 175, 199, 223, file)
    # N(13) and n=885
    apply(13, 885, 101, 295, 489, file)
    # N(14) and n=1425
    apply(14, 1425, 206, 475, 744, file)
