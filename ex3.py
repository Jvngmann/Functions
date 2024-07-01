def solve_t(heads, legs):

    for C in range(heads + 1):
        R = heads - C
        if 2 * C + 4 * R == legs:
            return C, R
    return None, None  

heads = 35
legs = 94
chickens, rabbits = solve_t (heads, legs)
print(f"Amount of chickens: {chickens}")
print(f"Amount of rabbits: {rabbits}")
