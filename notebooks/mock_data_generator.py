import pandas as pd
from faker import Faker
from random import randrange
from datetime import datetime

MIN_NUM_TITLES = 5
MAX_NUM_TITLES = 10

class MockDataGenerator:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_random_title(self):
        return self.dataset.sample(n=1)['title'].values[0]

    def generate_mock_data(self, num_rows):
        fake = Faker()
        fake_data = []

        for i in range(num_rows):
            fake_row = {
                'username': fake.name(),
                'country': fake.country(),
                'title': self.get_random_titles(num_titles=randrange(MIN_NUM_TITLES, MAX_NUM_TITLES)),
                'date_watched': fake.date_between_dates(date_start=datetime(2000,1,1), date_end=datetime(2023,1,1)).year,
                'percentage_watched': fake.random_int(0, 100),
                'rating': fake.random_int(1, 10)
            }
            fake_data.append(fake_row)

        return pd.DataFrame(fake_data)

    def get_random_titles(self, num_titles):
        return self.dataset.sample(n=num_titles)['title'].values

def main():
    
    dataset = pd.read_csv('/Users/burak/Developer/MachineLearning/4462 - Final Project/dataset/netflix_titles.csv')
    mock_data_generator = MockDataGenerator(dataset)

    mock_data = mock_data_generator.generate_mock_data(15000)
    # convert mock data to csv
    mock_data.to_csv('mock_user_data.csv', index=False)
    

if __name__ == '__main__':
    main()