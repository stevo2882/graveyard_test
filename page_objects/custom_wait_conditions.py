

def webelement_to_be_clickable(element):
    """Return the element if clickable or False if not.

    :param element: The WebElement to look for clickability of.
    :return: The WebElement if visible, else False.
    """
    def check_clickability(driver):
        if element.is_displayed() and element.is_enabled():
            return element
        else:
            return False

    return check_clickability
