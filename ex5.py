def permute_string(input_string):

    def generate_permutations(current_permutation, remaining_characters):
        if len(remaining_characters) == 0:
            print(current_permutation)
        else:
            for i in range(len(remaining_characters)):
                new_permutation = current_permutation + remaining_characters[i]
                remaining_chars = remaining_characters[:i] + remaining_characters[i + 1:]
                generate_permutations(new_permutation, remaining_chars)

    generate_permutations("", input_string)


x = input()
permute_string(x)
