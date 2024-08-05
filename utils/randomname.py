import random
from utils.logger import log

def random_name():
    return '_'+''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))

