# colors for terminal output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Used to return specific element in kmap
def multiply(a, b, table):
    return table[a][b]

# If user decides to input their kmap manually
def get_user_input():
    table = []
    for i in range(4):
        row = []
        for j in range(4):
            value = int(input(f"{YELLOW}Enter value for position ({i}, {j}): {RESET}"))
            row.append(value)
        table.append(row)
    return table

def check_validity(table):
    is_commutative = True
    # used to check commutativity of multiplication
    for a in range(4):
        for b in range(4):
            if multiply(a, b, table) != multiply(b, a, table):
                is_commutative = False
                print(f"{RED}Multiplication is not commutative for a={a}, b={b}{RESET}")
            else:
                print(f"{GREEN}Multiplication is commutative for a={a}, b={b}{RESET}")

    # used to find identity element
    identity = None
    for e in range(4):
        is_identity = True
        for a in range(4):
            if multiply(e, a, table) != a or multiply(a, e, table) != a:
                is_identity = False
                break
        if is_identity:
            identity = e
            break

    if identity is not None:
        print(f"{GREEN}The identity element is: {identity}{RESET}")
    else:
        print(f"{RED}There is no identity element in the table.{RESET}")

    # Check if each element has exactly one inverse (complement)
    all_have_inverses = True
    if identity is not None:
        for a in range(4):
            inverse_count = 0
            for b in range(4):
                if multiply(a, b, table) == identity and multiply(b, a, table) == identity:
                    inverse_count += 1
            if inverse_count == 0:
                print(f"{RED}Element {a} does not have an inverse.{RESET}")
                all_have_inverses = False
            elif inverse_count > 1:
                print(f"{RED}Element {a} has more than one inverse.{RESET}")
                all_have_inverses = False
        
        if all_have_inverses:
            print(f"{GREEN}All elements have exactly one inverse.{RESET}")
        else:
            print(f"{RED}Not all elements have exactly one inverse.{RESET}")
    else:
        print(f"{RED}Cannot check inverses without an identity element.{RESET}")

    if is_commutative and identity is not None and all_have_inverses:
        print(f"{GREEN}This is a VALID Kmap!{RESET}")
    else:
        print(f"{RED}This is an INVALID Kmap!{RESET}")

# Main Menu for Kmap Insertion
print(f"{YELLOW}|~~ Choose an option (A or B) ~~|{RESET}")
print(f"{YELLOW}    A.  Manually enter all Kmap data per position{RESET}")
print(f"{YELLOW}    B.  Kmap Already Hardcoded into 'Table' variable (Runs Script Immediately){RESET}\n")

choice = input(f"{YELLOW}Enter your choice (A or B): {RESET}").strip().upper()
print()
if choice == 'A':
    table = get_user_input()
elif choice == 'B':
    table = [
        [0, 1, 2, 3], # 0
        [1, 2, 3, 0], # 1
        [2, 3, 3, 1], # 2
        [3, 0, 1, 0]  # 3
    ]
else:
    print(f"{RED}Invalid choice. Please enter 'A' or 'B'.{RESET}")
    exit(1)

print()
check_validity(table)
