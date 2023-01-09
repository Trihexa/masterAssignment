class Expedition:

    def __init__(self, id, name, mountain_id, start, date, country, duration, success) -> None:
        self.id = id
        self.name = name
        self.mountain_id = mountain_id
        self.start = start
        self.date = date  # change to datetime
        self.country = country
        self.duration = duration
        self.success = success

    def add_climber(self):
        pass

    def get_climbers(self):
        pass

    def get_mountain(self):
        pass

    def convert_date(self):
        pass

    def convert_duration(self):
        pass

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))
