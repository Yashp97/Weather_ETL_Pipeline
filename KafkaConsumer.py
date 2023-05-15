import json
from json import loads
from kafka import KafkaConsumer
from s3fs import S3FileSystem

def main():

    # Initiate KafkaConsumer
    public_ip = 'enter_public_ip_here'
    consumer = KafkaConsumer('demo_test',
                             bootstrap_servers=[f'{public_ip}:9092'],
                             value_deserializer=lambda x: loads(x.decode('utf-8')))

    # Write consumed data to S3 bucket
    s3 = S3FileSystem()
    bucket_name = 'enter_bucket_name'
    for c, i in enumerate(consumer):
        with s3.open(f's3://{bucket_name}/weather_'+'{}.json'.format(c), 'w') as file:
            json.dump(i.value, file)

if __name__ == '__main__':
    main()