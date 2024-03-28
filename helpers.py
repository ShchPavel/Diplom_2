import random
import string


class DataGenerator:
    @staticmethod
    def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(5))
        return random_string

    @staticmethod
    def generate_random_email():
        return f'{DataGenerator.generate_random_string()}@{DataGenerator.generate_random_string()}.{DataGenerator.generate_random_string()}'


print(DataGenerator.generate_random_string())
print(DataGenerator.generate_random_email())