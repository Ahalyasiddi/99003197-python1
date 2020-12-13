import re


class Profile:
    print(re.match("[A-Z][a-z]+", "Caloriecalculator"))

    def __init__(self):
        self.age = int(input('What is your age: '))
        self.gender = input('What is your gender: ')
        self.weight = int(input('What is your weight: '))
        self.height = int(input('What is your height in inches: '))
        self. bmr_result = 0
        self.activity = 0

    class Display:
        def __init__(self):
            self.name = input("Your Name Please!")

        def display(self):
            print("Hello")
            print(self.name)

    def Func(self):
        if self.gender == 'male':
            c1 = 66
            hm = 6.2 * self.height
            wm = 12.7 * self.weight
            am = 6.76 * self.age
        elif self.gender == 'female':
            c1 = 655.1
            hm = 4.35 * self.height
            wm = 4.7 * self.weight
            am = 4.7 * self.age
            self.bmr_result = c1 + hm + wm - am

    def calculate_activity(self):
        print('What is your activity level ')
        activity_level = input('(none, light, moderate, heavy, or extreme): ')

        if activity_level == 'none':
            self.activity = 1.2 * self.bmr_result
        elif activity_level == 'light':
            self.activity = 1.375 * self.bmr_result
        elif activity_level == 'moderate':
            self.activity = 1.55 * self.bmr_result
        elif activity_level == 'heavy':
            self.activity = 1.725 * self.bmr_result
        elif activity_level == 'extreme':
            self.activity = 1.9 * self.bmr_result
        print(self.activity)

    def gain_or_lose(self):
        goals = input('Do you want to lose, maintain, or gain weight: ')

        if goals == 'lose':
            calories = self.activity - 500
        elif goals == 'maintain':
            calories = self.activity
        elif goals == 'gain':
            gain = int(input('Gain 1 or 2 pounds per week? Enter 1 or 2: '))
        if gain == 1:
            calories = self.activity + 500
        elif gain == 2:
            calories = self.activity + 1000
        print('\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
        print('In order to ', goals)
        print('weight, your daily caloric goals should be', int(calories), '!')
        print(calories)
        print('\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')

obj = Profile()
obj1 = Profile.Display()
obj1.display()
obj.Func()
obj.calculate_activity()
obj.gain_or_lose()
