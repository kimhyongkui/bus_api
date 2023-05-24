import redis

redis_host = 'localhost'
redis_port = 6379


r = redis.Redis(host=redis_host, port=redis_port)

