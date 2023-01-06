from flask import Flask
from flask import request
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

@app.route("/api/temperature", methods=['POST'])
def temperature():
    if request.method == 'POST' :
        length = trame_length(request.data)
        if length == 6 :
            hex = getfirstdigit(request.data)
            data = transform_hex_to_dec(hex)
            write("Temp", data)
        elif length == 10 : 
            hex = getfirstdigit(request.data)
            data = transform_hex_to_dec(hex)
            write("Temp", data)
            hex = getlastdigit(request.data)
            data = transform_hex_to_dec(hex)
            write("Temp", data)
        return request.data

@app.route("/api/humidity", methods=['POST'])
def humidity():
    if request.method == 'POST' :
        length = trame_length(request.data)
        if length == 6 :
            hex = getfirstdigit(request.data)
            data = transform_hex_to_dec(hex)
            write("Hum", data)
        elif length == 10 : 
            hex = getfirstdigit(request.data)
            data = transform_hex_to_dec(hex)
            write("Hum", data)
            hex = getlastdigit(request.data)
            data = transform_hex_to_dec(hex)
            write("Hum", data)
        return request.data

def getfirstdigit(trame):
    split_one = str(trame).split(":")
    split_two = split_one[1].split("\"")
    return split_two[1][3:6]

def getlastdigit(trame):
    split_one = str(trame).split(":")
    split_two = split_one[1].split("\"")
    return split_two[1][7:10]

def transform_hex_to_dec(hex):
    return int(hex, 16) / 10 

def trame_length(trame):
     split_one = str(trame).split(":")
     split_two = split_one[1].split("\"")
     return len(split_two[1])
    

def write(name, value):

    bucket = "keyce"
    org = "keyce"
    token = "QxAtbrlZYSBYXqBjGPUBSpxtJl_sTkf3Q_KW1KLrLnGiEJqL8NCU12YQxhxXJ47CRi6MTQKMT_MamQNSQ2k0Ug=="
    # Store the URL of your InfluxDB instance
    url="http://localhost:8086"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    # Write script
    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = influxdb_client.Point("_measurement").field(name, value)
    write_api.write(bucket=bucket, org=org, record=p)
