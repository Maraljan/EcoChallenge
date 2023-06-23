import datetime


def convert_dt_to_str_without_tz(dt: datetime.datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%S')
