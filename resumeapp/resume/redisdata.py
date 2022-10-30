from email import message
import redis

redis_host = 'redis-15952.c13.us-east-1-3.ec2.cloud.redislabs.com'
redis_port = 15952
password = 'SFpUN6jluSIoLYPjuCwFT93rhYC75dpB'
r = redis.Redis(host = redis_host, port = redis_port, password = password)

def addValueToSet(setName, value):
    message = r.sadd(setName, value)
    return message

def removeValueFromSet(setName, value):
    message = r.srem(setName, value)
    return message

def findValueInSet(setName, value):
    message = r.sismember(setName, value)
    return message

def findAllSkillsInSet(setName):
    message = r.smembers(setName)
    messageDecoded = [i.decode() for i in message]
    return messageDecoded

def addValueToHash(hashName, key, value):
    message = r.hset(hashName, key, value)
    return message

def removeValueFromHash(hashName, key, value):
    message = r.hdel(hashName, key, value)
    return message

def findValueInHash(hashName, key):
    message = r.hexists(hashName, key)
    return message

def findKeysInHash(hashName):
    message = r.hkeys(hashName)
    keysDecoded = [i.decode() for i in message]
    return keysDecoded

def findAllValuesInHash(hashName):
    message = r.hvals(hashName)
    valsDecoded = [i.decode() for i in message]
    return valsDecoded

def findKeysAndValuesInHash(hashName):
    message = r.hgetall(hashName)
    jobTitles = {}
    for i in message:
        jobTitles[i.decode()] = message[i].decode()
    return jobTitles


#if __name__ == "__main__":
#    redis_string()
    