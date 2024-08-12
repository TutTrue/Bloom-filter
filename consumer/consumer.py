import redis
import sys
from bloom import BloomFilter

r = redis.Redis(host='redis', port=6379, db=0)


def receive_messages(bloom: BloomFilter):
    while True:
        result = r.brpop('my_queue', timeout=5)
        if result is None:
            break
        _, message = result
        bloom.add(message.decode('utf-8'))
        print(f"Received message: {message.decode('utf-8')}", end='')
        sys.stdout.flush()


def send_message(queue_name, message):
    r.lpush(queue_name, message)
    print(f"Sent message: {message}", end='')
    sys.stdout.flush()


def consume(bloom: BloomFilter):
    receive_messages(bloom)


if __name__ == '__main__':
    bloom = BloomFilter()
    consume(bloom)

    send_message('agg-queue', str(bloom))

    print('done')
    