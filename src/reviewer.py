def review_code(code):

    feedback = []
    score = 100

    if "print(" in code:
        feedback.append(
            "Avoid unnecessary print statements. Use proper logging in production code."
        )
        score -= 10

    if "def " in code and '"""' not in code:
        feedback.append(
            "Functions should include docstrings for better readability."
        )
        score -= 10

    if "," in code and ", " not in code:
        feedback.append(
            "Follow PEP8 style: Add spaces after commas."
        )
        score -= 10

    for line in code.split("\n"):
        if len(line) > 79:
            feedback.append(
                "Line length exceeds 79 characters."
            )
            score -= 10
            break

    if not feedback:
        feedback.append("No major issues found. Code looks good!")

    report = f"""
====================================
       AI CODE REVIEW REPORT
====================================

Code Quality Score: {score}/100

Issues Found: {len(feedback)}

"""

    for index, issue in enumerate(feedback, 1):
        report += f"{index}. {issue}\n"

    report += """
====================================
"""

    return report