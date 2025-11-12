class PersonalInformationManager:
    def __init__(self, name, age, city, hobbies):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = hobbies

    def display_info(self):
        print("=" * 40)
        print("      PERSONAL INFORMATION MANAGER")
        print("=" * 40)
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"City    : {self.city}")
        print("Hobbies :")
        for i, hobby in enumerate(self.hobbies, start=1):
            print(f"  {i}. {hobby}")
        print("=" * 40)

if __name__ == "__main__":
    name = "Vansh"
    age = 19
    city = "Kanpur"
    hobbies = ["Sports", "Writing", "Reading"]

    pim = PersonalInformationManager(name, age, city, hobbies)
    pim.display_info()
