def celsius_converter(f_temp):
    return round((float(f_temp) - 32)/1.8, 2)

def parse_and_clean(line):
    if line.count("|") != 4:
        return None

    try:
        Timestamp, StationID, Temp, Humidity, Sensor_Status = line.split("|")
    except ValueError:
        return None

    Timestamp = Timestamp.strip()
    StationID = StationID.strip()
    Temp = Temp.strip()
    Humidity = Humidity.strip()
    Sensor_Status = Sensor_Status.strip()

    if (not Timestamp or not StationID or not Temp or
        not Humidity or not Sensor_Status):
        return None

    if Temp in ("ERROR", "N/A"):
        return None

    if Sensor_Status != "ACTIVE":
        return None

    return Timestamp, StationID, Temp, Humidity, Sensor_Status

def main():

    err = 0

    with open("C:/Users/Arnas/Downloads/environmental_raw.txt", "r") as input, \
         open("environmental_clean.csv", "w") as output:

        for line in input:
            cleaned = parse_and_clean(line)

            if cleaned is None:
                err += 1
                continue

            Timestamp, StationID, Temp, Humidity, Sensor_Status = cleaned
            Temp = celsius_converter(Temp)

            output.write(
                f"{Timestamp},{StationID},{Temp},{Humidity},{Sensor_Status}\n"
            )

    print("Number of corrupted lines:", err)

if __name__ == "__main__":
    main()