
class BaseTest:

    driver = None
    general = None

    def __init__(self, driver, parent_handle):
        self.driver = driver
        self.parent_handle = parent_handle