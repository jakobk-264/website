"""A collection of all related functions in the CV blueprint"""

from . import model
from .data import jakob


def get_cv_by_Name(name: str) -> model.CvEntry:
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
