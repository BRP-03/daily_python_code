import os
import json
from datetime import date
from google import genai

client=genai.Client(api_key=os.environ["AIzaSyBfACGMPG3theqoJyIW7T42u_kQpBn93pk"])
STATE="state.json"

with open(
    STATE,
    "r"
) as f:

    state=json.load(f)

current=state[
    "current_problem"
]

with open(
    "problems.txt",
    "r",
    encoding="utf8"
) as f:

    problems=f.readlines()

problem=problems[
    current
].strip()

prompt=f"""

Create complete python project.

Problem:

{problem}

Requirements:

1 Complete code

2 Add comments

3 Beginner friendly

Only output code.

"""

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

code=response.text

code=code.replace(
    "```python",
    ""
)

code=code.replace(
    "```",
    ""
)

folder=f"generated_projects/Day_{current+1}"

os.makedirs(
    folder,
    exist_ok=True
)

with open(
    f"{folder}/main.py",
    "w",
    encoding="utf8"
) as f:

    f.write(code)

readme=f"""

# Day {current+1}

Problem:

{problem}

Generated:
{date.today()}

"""

with open(
    f"{folder}/README.md",
    "w"
) as f:

    f.write(readme)

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