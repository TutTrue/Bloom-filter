import redis
import sys

r = redis.Redis(host='redis', port=6379, db=0)

def send_message(queue_name, message):
    r.lpush(queue_name, message)
    print(f"Sent message: {message}", end='')
    sys.stdout.flush()

def produce():
    with open('data-bloom.txt', 'r') as f:
        for i, l in enumerate(f.readlines()):
            send_message('my_queue', f'{i}: {l}')

if __name__ == '__main__':
    produce()