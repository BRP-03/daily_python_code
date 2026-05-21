import json
import os

STATE = "state.json"

programs = [

('''

num = int(
    input(
        "Enter number: "
    )
)

if num % 2 == 0:

    print(
        "Even"
    )

else:

    print(
        "Odd"
    )

''',"Even Odd Checker"),

('''

text = input()

if text == text[::-1]:

    print(
        "Palindrome"
    )

else:

    print(
        "Not palindrome"
    )

''',"Palindrome Checker"),

('''

n=int(input())

fact=1

for i in range(
    1,
    n+1
):

    fact*=i

print(
    fact
)

''',"Factorial"),

('''

a=0
b=1

for i in range(
    10
):

    print(
        a
    )

    a,b=b,a+b

''',"Fibonacci"),

('''

text=input()

print(
    text[::-1]
)

''',"Reverse String"),

('''

a=int(input())

b=int(input())

print(
    a+b
)

''',"Calculator"),

('''

for i in range(
    1,
    11
):

    print(
        i*i
    )

''',"Squares"),

('''

nums=[1,5,3,7]

print(
    max(nums)
)

''',"Max Finder"),

('''

for i in range(
    1,
    6
):

    print(
        "*"*i
    )

''',"Pattern"),

('''

password="abc123"

user=input()

print(
    user==password
)

''',"Password Check")

]

with open(
    STATE,
    "r"
) as f:

    state=json.load(
        f
    )

current=state[
    "current_problem"
]

code,title=programs[
    current % len(
        programs
    )
]

folder=f"generated_projects/program{current+1}"

os.makedirs(
    folder,
    exist_ok=True
)

with open(
    f"{folder}/main.py",
    "w"
) as f:

    f.write(
        code
    )

with open(
    f"{folder}/README.md",
    "w"
) as f:

    f.write(
        f"# {title}"
    )

state[
    "current_problem"
]+=1

with open(
    STATE,
    "w"
) as f:

    json.dump(
        state,
        f,
        indent=4
    )

print(
    "Done"
)