import requests
import json
from json import dumps,loads
from time import sleep
from kafka import KafkaConsumer
from datetime import datetime
import pandas as pd

def main():

    public_ip = '18.224.5.231'
    consumer = KafkaConsumer('demo_test',
                             bootstrap_servers=[f'{public_ip}:9092'],
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    for c in consumer:
        print(c.value)

if __name__ == '__main__':
    main()