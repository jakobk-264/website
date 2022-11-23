"""A place holder module in lieu of any more advanced data storage"""


from . import model
from datetime import date

##### Data for Jakob
jk_personal = model.Personal(
    name="Jakob Kisiala",
    email="****.****@tuta.io",
    phone="+44 (0) 7722 XXX XXX",
    location="Edinburgh, UK",
    immigration_status="Right to work in the UK and EU",
    about_me="Currently, I am working as risk consultant advising "
    "customers with a focus on quantitative risk management questions, "
    "such as model development, model validation, and model risk management. ",
)

jk_employment = [
    model.Employment(
        start_date=date(2022, 8, 1),
        end_date=date.today(),
        employer="True North Partners",
        employer_description="An independent consulting firm specialising in finance, risk, and strategy consulting for financial institutions in the UK, Central Europe, South Africa, and the Middle East.",
        employer_homepage="https://tnp.eu/",
        job_title="Manager",
        location="UK (Remote)",
    ),
    model.Employment(
        start_date=date(2020, 3, 1),
        end_date=date(2022, 7, 31),
        employer="NatWest Group",
        employer_description="A Systemically Important Bank in the UK with a comprehensive Retail and Commercial banking offering.",
        employer_homepage="https://www.natwestgroup.com/",
        job_title="Senior Model Risk Quant",
        team_name="Machine Learning and Automation Model Risk",
        location="Edinburgh, UK",
        responsibilities=[
            "Deputy team lead for a team of 6 people",
            "Lead model risk manager for fraud prevention models",
        ],
    ),
    model.Employment(
        start_date=date(2017, 11, 1),
        end_date=date(2020, 2, 28),
        employer="NatWest Group",
        employer_description="A Systemically Important Bank in the UK with a comprehensive Retail and Commercial banking offering.",
        employer_homepage="https://www.natwestgroup.com/",
        job_title="Model Risk Quant",
        team_name="Wholesale and Retail Credit Model Risk",
        location="Edinburgh, UK",
    ),
    model.Employment(
        start_date=date(2016, 4, 4),
        end_date=date(2017, 10, 31),
        employer="NatWest Group",
        employer_description="A Systemically Important Bank in the UK with a comprehensive Retail and Commercial banking offering.",
        employer_homepage="https://www.natwestgroup.com/",
        job_title="Senior Analyst",
        team_name="Operational Risk Modelling",
        location="Edinburgh, UK",
    ),
]

jk_projects = [
    model.Project(
        date=date(2022, 11, 23),
        description="Building a personal website and blog with Flask and hosting it using AWS Elastic Beanstalk.",
        portfolio_link="https://github.com/jakobk-264/website",
    ),
    model.Project(
        date=date(2021, 1, 1),
        description="Validation of different vendor and in-house developed fraud prevention models for credit cards, online payments, and vulnerable customers.",
    ),
    model.Project(
        date=date(2015, 8, 31),
        description="MSc Dissertation about the theory and application of Conditional Value-at-Risk",
        portfolio_link="https://arxiv.org/abs/1511.00140",
    ),
]

jk_education = [
    model.Education(
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
    model.Qualification(
        date=date(2018, 11, 1),
        qualification_name="Financial Risk Manager (FRM)",
        issuing_institution="GARP",
        evidence_link="https://my.garp.org/DigitalBadgeFRM?id=0034000001tMcW9AAK",
    )
]

jk_skills = [
    model.Skill(name="Python", category="Coding", level="Advanced"),
    model.Skill(name="Flask", category="Coding", level="Beginner"),
]

jakob = model.CvEntry(
    personal=jk_personal,
    employment_history=jk_employment,
    projects=jk_projects,
    education=jk_education,
    qualifications=jk_qualification,
    skills=jk_skills,
)
