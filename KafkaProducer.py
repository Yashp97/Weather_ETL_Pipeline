from json import dumps
from time import sleep
from kafka import KafkaProducer
import pandas as pd


def main():

    # Read and Clean Data
    df = pd.read_csv('temperature.csv')
    df.dropna(inplace=True)
    df.iloc[:,1:] = df.iloc[:,1:].apply(convert_K_to_F)

    # Initiate KafkaProducer Based on EC2 Public IP
    public_ip = 'enter_public_ip_here'
    producer = KafkaProducer(bootstrap_servers=[f'{public_ip}:9092'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))

    # Loop Through Each Temperature Data Point -- simulate real time temperature data
    while True:
        for n in range(len(df)):
            sample = df.iloc[n].to_dict()
            producer.send('demo_test', value=sample)
            sleep(1)

def convert_K_to_F(K):
    return (K - 273.15) * 1.8 + 32

if __name__ == '__main__':
    main()