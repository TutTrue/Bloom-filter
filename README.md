# Bloom Filter

This project demonstrates a simple Bloom filter implementation using Redis and Docker. The setup consists of a producer that generates IP addresses and multiple consumers that aggregate these addresses into a single Bloom filter.

### Components

- **Producer**: Reads a file with generated IP addresses and publishes them to a Redis queue.
- **Consumers**: Ten consumers retrieve IP addresses from the Redis queue and add them to a Bloom filter object.
- **Aggregation**: After processing, all Bloom filter objects are combined using the bitwise OR operation to create a single Bloom filter.

### Setup and Execution

1. **Prepare Data**: 
   Navigate to the `producer` directory and generate the IP address data.
   
   ```bash
   cd producer
   python3 create_data.py
   cd ..
   ```

2. **Start Services**:
   Use Docker Compose to build and start the necessary services.

   ```bash
   sudo docker-compose up --build
   ```

### Configuration

- **Bloom Filter Settings**:
  Don’t forget to adjust the Bloom filter hash functions and size in the consumer. You can use the [Bloom filter calculator](https://hur.st/bloomfilter/?n=1000000&p=1.0E-7&m=&k=) to determine the optimal parameters based on your dataset size and desired false positive rate.

### Output
- The final aggregated Bloom filter will be stored in the `aggregation/data-agg.py` file.

### Requirements

- Docker
- Docker Compose
- Python 3

Make sure you have these prerequisites installed on your system before running the setup.
