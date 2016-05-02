from db import session
from db.models import VIN, CarNum

def get_vin():
    raw_val = str(input())
    try:
        VIN.validate_vin(raw_val)
    except ValueError as e:
        print(e)
        return None
    return VIN(raw_val)


if __name__ == '__main__':
    get_vin()