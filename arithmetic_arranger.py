test_arr = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


def arithmetic_arranger(problems, results=False):
    a = []
    b = []
    c = []
    length = len(problems)
    top = []
    middle = []
    res = []
    dashes = []
    whitespace = "    "

    # Checking validity of array
    if length > 5 or (len(a) > 5 or len(b) > 5 or len(c) > 5):
        return "Error: Too many problems."

    for i in range(length):
        problems[i] = problems[i].split()
        a.append(problems[i][0])
        b.append(problems[i][1])
        c.append(problems[i][2])

    for _ in range(len(problems)):
        if not a[_].isdigit() or not c[_].isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(a[_]) > 4 or len(c[_]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif b[_] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
    # END OF CHECKING

    # First line formatting and appending

    for first in range(length):
        if len(a[first]) == len(c[first]) or len(a[first]) > len(c[first]):
            top.append(a[first].rjust(len(a[first]) + 2))
        elif len(a[first]) < len(c[first]):
            top.append(a[first].rjust(len(c[first]) + 2))

    # Second line formatting and appending
    for second in range(length):
        if len(a[second]) == len(c[second]) or len(a[second]) > len(c[second]):
            middle.append(b[second] + " " + c[second].rjust(len(a[second])))
        elif len(a[second]) < len(c[second]):
            middle.append(b[second] + " " + c[second].rjust(len(c[second])))

    # third line formatting and appending

    for third in range(length):
        if len(a[third]) > len(c[third]):
            dashes.append("-" * (len(a[third]) + 2))
        else:
            dashes.append("-" * (len(c[third]) + 2))

    # Result of calculations formatting and appending
    if results:
        for s in range(length):
            total_sum = None
            if b[s] == "+":
                total_sum = int(a[s]) + int(c[s])
            elif b[s] == "-":
                total_sum = int(a[s]) - int(c[s])
            res.append(str(total_sum).rjust(len(dashes[s])))

    # Constructing lines from arrays

    first_line = whitespace.join(top)
    second_line = whitespace.join(middle)
    third_line = whitespace.join(dashes)
    res_line = whitespace.join(res)

    # Constructing returned variable - rstrip necessary for corrept submit.
    arranged_problems = first_line + "\n" + second_line + "\n" + third_line + "\n"

    if results:
        return arranged_problems + res_line + "\n".rstrip()

    return arranged_problems.rstrip()


print(arithmetic_arranger(test_arr, True))