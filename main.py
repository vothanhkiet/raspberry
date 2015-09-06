from pubnub import Pubnub
import time
import psutil
import os


def callback(message):
    print(message)


def main():
    publish_key = os.environ['PUBNUB_PUBLISH_KEY']
    subscribe_key = os.environ['PUBNUB_SUBSCRIBE_KEY']
    pubnub = Pubnub(publish_key, subscribe_key, ssl_on=False)
    cpu_count = psutil.cpu_count()
    try:
        while True:
            cpu = str(psutil.cpu_percent() / cpu_count)
            pubnub.publish(channel="kiettv.raspberry.os", message=cpu, callback=None, error=callback)
            time.sleep(1)
    except KeyboardInterrupt:
        pubnub.unsubscribe(channel='kiettv.raspberry.os')
        exit(0)


if __name__ == '__main__':
    main()
