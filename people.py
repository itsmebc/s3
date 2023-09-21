import pandas as pd
import random
from faker import Faker

fake = Faker()

for x in range(1,6):
    def generate_fake_data(total):
        people = []

        for i in range(total):
            students.append({
                "group": random.randint(1,20),
                "firstname": fake.first_name(),
                "buildingnumber": fake.building_number(),
                "streetname": fake.street_name(),
                "streetname2": fake.street_suffix(),
                "country": fake.country(),
                "country_code": fake.country_code(),
                "post": fake.postalcode(),
                "occupation": fake.job(),
                "LASTNAME": fake.last_name()
            })    

        return people  

    df = pd.DataFrame(generate_fake_data(1000))

    def columns_transformation(dataframe):
        dataframe.columns = dataframe.columns.str.upper()
        dataframe["ADDRESS"] = dataframe["BUILDINGNUMBER"] + " " + dataframe["STREETNAME"] + " " + dataframe["STREETNAME2"] + ", " + dataframe["COUNTRY_CODE"] + " " + dataframe["POST"]
        dataframe["FULL_NAME"] = dataframe["FIRSTNAME"] + " " + dataframe["LASTNAME"]
        dataframe[["CAREER", "SPECIALIZATION"]] = dataframe["OCCUPATION"].str.split(',', expand=True)
        dataframe = dataframe.iloc[:,[0,11,10,12,13]]
        return dataframe


    df_cleaned = columns_transformation(df)
    iteration = str(x)
    df_cleaned.to_csv('s3://*************/data_' + iteration + '.csv', index=False)