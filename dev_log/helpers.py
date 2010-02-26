import datetime


from sys import version_info

def parse_datetime(str_date):
    str_date = str_date[:-6]
    if version_info[0] == 1 or (version_info[0] == 2 and version_info[1] < 6):
        partitioned = str_date.split("T")
        date = partitioned[0].split("-")
        time = partitioned[1].split(":")
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        hour = int(time[0])
        minute = int(time[1])
        second = int(time[2])
        return datetime.datetime(year, month, day, hour, minute, second)

        # "timestamp": "2008-02-15T14:36:34-08:00"
    else:
        return datetime.datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S")
