from datetime import datetime, timedelta


def get_requests():
    import requests

    print(f"Requestes: {requests.__version__}")


def get_beatiful():
    import bs4

    print(f"bs4: {bs4.__version__}")


#### just testing


def sum_print():
    print(sum([1, 2, 3]))
