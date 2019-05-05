def wipe_database(redis):
    for key in redis.keys('*'):
        redis.delete(key)
