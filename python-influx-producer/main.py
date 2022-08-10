import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

import os
from dotenv import load_dotenv



def main():
    load_dotenv()

    influx_bucket = os.getenv("INFLUXDB_BUCKET")
    influx_org = os.getenv("INFLUXDB_ORG")
    influx_token = os.getenv("INFLUXDB_TOKEN")
    # Store the URL of your InfluxDB instance
    influx_url="http://localhost:8086"

    client = influxdb_client.InfluxDBClient(
        url=influx_url,
        token=influx_token,
        org=influx_org
    )
    write_api = client.write_api(write_options=SYNCHRONOUS)
    while True:
        x = random.random()
        # Random float number
        numb = random.uniform(1, 90000)
        p = influxdb_client.Point("my_measurement").tag("sensor","data").field("temperature", numb)
        write_api.write(bucket=influx_bucket, org=influx_org, record=p)
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


