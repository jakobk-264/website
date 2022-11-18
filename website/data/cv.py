from website.model import cv
from datetime import date

##### Data for Jakob
jk_personal = cv.Personal(
    name="Jakob Kisiala",
    email="****.****@tuta.io",
    phone="+44 (0) 7722 XXX XXX",
    location="Edinburgh, UK",
    immigration_status="Right to work in the UK and EU",
)

jk_employment = [
    cv.Employment(
        start_date=date(2022, 8, 1),
        end_date=date.today(),
        employer="True North Partners",
        job_title="Manager",
        location="Remote, UK",
    ),
    cv.Employment(
        start_date=date(2020, 3, 1),
        end_date=date(2022, 7, 31),
        employer="NatWest Group",
        job_title="Senior Model Risk Quant",
        team_name="Machine Learning and Automation Model Risk",
        location="Edinburgh, UK",
    ),
    cv.Employment(
        start_date=date(2017, 11, 1),
        end_date=date(2020, 2, 28),
        employer="NatWest Group",
        job_title="Model Risk Quant",
        team_name="Wholesale and Retail Credit Model Risk",
        location="Edinburgh, UK",
    ),
    cv.Employment(
        start_date=date(2016, 4, 4),
        end_date=date(2017, 10, 31),
        employer="NatWest Group",
        job_title="Senior Analyst",
        team_name="Operational Risk Modelling",
        location="Edinburgh, UK",
    ),
]

jk_projects = [
    cv.Project(
        date=date(2021, 1, 1),
        description="Validation of different vendor and in-house developed fraud prevention models for credit cards, online payments, and vulnerable customers.",
    ),
    cv.Project(
        date=date(2015, 8, 31),
        description="MSc Dissertation about the theory and application of Conditional Value-at-Risk",
        portfolio_link="https://arxiv.org/abs/1511.00140",
    ),
]

jk_education = [
    cv.Education(
        start_date=date(2014, 9, 1),
        end_date=date(2015, 8, 31),
        institution="University of Edinburgh",
        degree="Operational Research (with distinction)",
        location="Edinburgh, UK",
        courses=[
            "Mathematical Optimisation",
            "Probability and Statistics",
            "Credit Scoring",
            "Optimisation Methods in Finance",
        ],
    )
]

jk_qualification = [
    cv.Qualification(
        date=date(2018, 11, 1),
        qualification_name="Financial Risk Manager (FRM)",
        issuing_institution="GARP",
        evidence_link="https://my.garp.org/DigitalBadgeFRM?id=0034000001tMcW9AAK",
    )
]

jk_skills = [
    cv.Skill(name="Python", category="Coding", level="Advanced"),
    cv.Skill(name="Flask", category="Coding", level="Beginner"),
]

jakob = cv.CvEntry(
    personal=jk_personal,
    employment_history=jk_employment,
    projects=jk_projects,
    education=jk_education,
    qualifications=jk_qualification,
    skills=jk_skills,
)


def cv_by_Name(name: str) -> cv.CvEntry:
    """Function to mimic the behaviour of a db request

    Args:
        name (str): The name of the person whose CV you want

    Returns:
        cv.CvEntry: The CV information of the person
    """
    if name == "Jakob Kisiala":
        return jakob.dict()
    else:
        return None


if __name__ == "__main__":
    print(jakob)
