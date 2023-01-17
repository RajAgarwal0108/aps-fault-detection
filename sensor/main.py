from sensor.exception import  SensorException
import sys

def test():
    try:
        return (3/0)
    except Exception as e:
        raise SensorException(e, sys)


if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        print(str(e))