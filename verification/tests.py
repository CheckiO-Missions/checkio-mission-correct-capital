"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["Checkio"],
            "answer": True
        },
        {
            "input": ["CheCkio"],
            "answer": False
        },
        {
                "input": ["CHECKIO"],
            "answer": True
        }
    ],
    "Extra": [
        {
            "input": ["pAymlGNhBZZZZ"],
            "answer": False
        },
        {
            "input": ["JAqXyPYYJC"],
            "answer": False
        },
        {
            "input": ["OcmbBqzYmsdaahb"],
            "answer": False
        },{
            "input": ["zmyxetssdfhif"],
            "answer": True
        },
        {
            "input": ["ooooooooooooooo"],
            "answer": True
        },
        {
            "input": ["ooooooooooooooO"],
            "answer": False
        },
        {
            "input": ["Normal"],
            "answer": True
        },
        {
            "input": ["NORMALLL"],
            "answer": True
        },
        {
            "input": ["USA"],
            "answer": True
        },
        {
            "input": ["n"],
            "answer": True
        }
    ]
}
