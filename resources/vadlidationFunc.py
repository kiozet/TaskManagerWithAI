def emailValidation(email: str) -> bool:
    """Base emai validation func, returns True if all is ok
    args: email: str"""

    if email.count("@") == 1 and email.count(".") == 1:  # write with fnmatch
        return True

    else:
        return False
