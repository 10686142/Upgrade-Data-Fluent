from pathlib import Path
from os import environ
from pprint import pprint

from csci_utils.canvas.canvas_helpers import pset_submission
from git import Repo

# Constants for this pset
COURSE_NAME = "Advanced Python for Data Science"
ASSIGNMENT = "Final Project"
QUIZ_NAME = "Test Quiz"


def print_quiz_questions(questions):
    """Prints actual json questions, to help develop"""

    for q in questions:
        print("{} - {}".format(q.question_name, q.question_text.split("\n", 1)[0]))

        # MC and some q's have 'answers' not 'answer'
        pprint(
            {
                k: getattr(q, k, None)
                for k in ["question_type", "id", "answer", "answers"]
            }
        )

        print()


def submit_project():

    with pset_submission(
        COURSE_NAME,
        ASSIGNMENT,
        QUIZ_NAME,
        allow_dirty=True,
        submit_assignment=True,
    ) as (questions, qsubmission):
        print_quiz_questions(questions)

        # Send back questions for test submission
        pset_answers = questions
        # # pprint(pset_answers)

        # # Fill out the answers and make the actual submission
        res = qsubmission.answer_submission_questions(quiz_questions=pset_answers)

    print(f"Full {ASSIGNMENT} submission complete!")


# Make our submission
submit_project()
