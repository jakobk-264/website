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
    model.Employment(
        start_date=date(2015, 9, 5),
        end_date=date(2016, 3, 31),
        employer="Barclays Capital Services",
        employer_homepage="https://www.cib.barclays/",
        job_title="Analyst",
        team_name="Banking Book and Grading Controls",
        location="Glasgow, UK",
    ),
    model.Employment(
        start_date=date(2014, 1, 1),
        end_date=date(2014, 6, 30),
        employer="Deutsche Bank",
        employer_homepage="https://www.db.com/",
        job_title="Intern",
        team_name="Retail Credit Risk Portfolio Reporting",
        location="Frankfurt Germany",
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
        description="Model validation of different vendor and in-house developed fraud prevention models for credit cards, online payments, and vulnerable customers.",
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
        degree="MSc in Operational Research (with distinction)",
        location="Edinburgh, UK",
        courses=[
            "Mathematical Optimisation",
            "Probability and Statistics",
            "Credit Scoring",
            "Optimisation Methods in Finance",
        ],
    ),
    model.Education(
        start_date=date(2007, 1, 1),
        end_date=date(2013, 12, 31),
        institution="Open University",
        degree="BSc (Honours) in Mathematics (1st class)",
        location="Milton Keynes, UK",
        courses=[
            "Pure Mathematics",
            "Complex Analysis",
            "Optimization",
            "Applications of Probability",
        ],
    ),
    model.Education(
        start_date=date(2006, 10, 1),
        end_date=date(2009, 9, 30),
        institution="Baden-Württemberg Cooperative State University",
        degree="BEng in Industrial Engineering",
        location="Stuttgart, Germany",
        courses=[
            "Production Systems",
            "Logistics Management",
            "Business Administration",
            "Mechanical Engineering",
        ],
    ),
]

jk_qualification = [
    model.Qualification(
        date=date(2020, 6, 23),
        qualification_name="AWS Certified Cloud Practitioner",
        issuing_institution="Amazon Web Services",
        evidence_link="https://www.credly.com/badges/0c9b85cd-4071-414f-8087-0c30240f338d/linked_in_profile",
    ),
    model.Qualification(
        date=date(2018, 11, 1),
        qualification_name="Financial Risk Manager (FRM)",
        issuing_institution="GARP",
        evidence_link="https://my.garp.org/DigitalBadgeFRM?id=0034000001tMcW9AAK",
    ),
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
