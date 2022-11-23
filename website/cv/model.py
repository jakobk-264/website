"""The CV data model"""

from typing import Optional
from pydantic import BaseModel, HttpUrl
from datetime import date


class Personal(BaseModel):
    """Any personal information"""

    name: str
    email: str
    phone: str
    location: str
    immigration_status: str
    about_me: str


class Employment(BaseModel):
    """Details on employment history"""

    start_date: date
    end_date: date
    employer: str
    employer_description: Optional[str] = None
    employer_homepage: Optional[HttpUrl] = None
    job_title: str
    team_name: Optional[str] = None
    location: str
    responsibilities: list[str] = []


class Project(BaseModel):
    """Any completed projects / portfolio"""

    date: date
    description: str
    portfolio_link: Optional[HttpUrl]


class Education(BaseModel):
    """Formal education"""

    start_date: date
    end_date: date
    institution: str
    degree: str
    location: str
    courses: list[str] = []


class Qualification(BaseModel):
    """Any additional qualifications"""

    date: date
    qualification_name: str
    issuing_institution: str
    evidence_link: HttpUrl


class Skill(BaseModel):
    """Any skills / frameworks that I have / know (keywords)"""

    name: str
    category: str
    level: str


class CvEntry(BaseModel):
    """The structure of a CV entry"""

    personal: Personal
    employment_history: list[Employment]
    projects: Optional[list[Project]]
    education: Optional[list[Education]]
    qualifications: Optional[list[Qualification]]
    skills: Optional[list[Skill]]
