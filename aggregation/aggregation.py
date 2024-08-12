import redis
import sys

r = redis.Redis(host='redis', port=6379, db=0)


def receive_messages():
    bloom = 0
    while True:
        _, message = r.brpop('agg-queue')
        bloom |= int(message.decode('utf-8'), 2)
        print(f"Received message: {message.decode('utf-8')}", end='')
        sys.stdout.flush()
        with open('data-agg.txt', '+w') as f:
            f.write(str(bloom))



def aggregate():
    receive_messages()


if __name__ == '__main__':
    aggregate()
    