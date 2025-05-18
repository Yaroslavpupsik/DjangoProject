class Yaroslav:
    def __init__(self, name=None, surname=None, birth_year=None, course=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.course = course

    def get_info(self):
        course_info = (
            self.course if isinstance(self.course, int) and self.course < 5 else "Випускник або невідомо"
        )
        return f"Ім'я: {self.name or 'Невідомо'} {self.surname or ''}, Рік народження: {self.birth_year or 'Невідомо'}, Курс: {course_info}"

    @staticmethod
    def get_names_list(students):
        return [f"{student.name or 'Імʼя невідоме'} {student.surname or 'Прізвище невідоме'}" for student in students]


class Onl_Yaroslav(Yaroslav):
    def __init__(self, name=None, surname=None, birth_year=None, course=None, online_platform=None, in_ukraine=None, device_used=None):
        super().__init__(name, surname, birth_year, course)
        self.online_platform = online_platform
        self.in_ukraine = in_ukraine
        self.device_used = device_used

    def _get_platform_info(self):
        return f"Online platform: {self.online_platform}"

    def _device_info(self):
        return f"Device used: {self.device_used}"

    def get_info(self):
        basic_info = super().get_info()
        platform_info = f", Платформа: {self.online_platform or 'Невідомо'}"
        location_info = f", За кордоном: {'Так' if self.in_ukraine is False else 'Ні'}"
        return basic_info + platform_info + location_info


# Створення об'єктів
Student1 = Yaroslav("Діма", "Поліщук", 2008)
Student2 = Yaroslav("Дімон", None, 2000)
Student3 = Yaroslav("Дмітрій", "Поляков", 2007, 2)

Student4 = Onl_Yaroslav("Діма", "Панчук", 2005, 3, "Zoom", False, "ПК")
Student5 = Onl_Yaroslav("Дімон", "Поліщук", 2008, 3, "Google Meet", True, "Ноутбук")

# Список студентів
Students = [Student1, Student2, Student3, Student4, Student5]
Names_list = Yaroslav.get_names_list(Students)

# Виведення результатів
print("Список імен:")
print(Names_list)
print()

print(Student1.get_info())
print(Student2.get_info())
print(Student3.get_info())
print(Student4.get_info())
print(Student5.get_info())
