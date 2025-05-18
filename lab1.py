class Taras_sigma:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        if age == 16:
            return 1  # 1 курс
        elif age == 17:
            return 2  # 2 курс
        return None

    def create_name_list(self):
        if self.first_name is None or self.last_name is None:
            return []
        return [self.first_name, self.last_name] 
    
