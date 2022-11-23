"""A collection of all related functions in the CV blueprint"""

from . import model


def get_cv_by_Name(name: str) -> model.CvEntry:
    """Function to mimic the behaviour of a db request

    Args:
        name (str): The name of the person whose CV you want

    Returns:
        cv.CvEntry: The CV information of the person
    """
    from .data import jakob

    if name == "Jakob Kisiala":
        return jakob
    else:
        None


if __name__ == "__main__":
    name = "Jakob Kisiala"
    response = get_cv_by_Name(name)
    print(response)
