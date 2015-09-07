import time
import os

from pubnub import Pubnub

from modules import system


def callback(message):
    print(message)


def main():
    publish_key = os.environ['PUBNUB_PUBLISH_KEY']
    subscribe_key = os.environ['PUBNUB_SUBSCRIBE_KEY']
    pubnub = Pubnub(publish_key, subscribe_key, ssl_on=False)
    try:
        cpu = system.SystemInfo()
        while True:
            pubnub.publish(channel="kiettv.raspberry.os", message=cpu.get_cpu_percent(), callback=None, error=callback)
            time.sleep(1)
    except KeyboardInterrupt:
        pubnub.unsubscribe(channel='kiettv.raspberry.os')
        exit(0)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    main()
