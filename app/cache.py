import time

# In-memory cache
cache = {}
CACHE_TTL = 3600  # Time to live for cache in seconds (1 hour)

def is_cache_valid(cache_key):
    """Check if the cache is still valid for the given key."""
    if cache_key in cache:
        data, timestamp = cache[cache_key]
        if time.time() - timestamp < CACHE_TTL:
            return data
    return None

def update_cache(cache_key, data):
    """Update cache with new data and timestamp."""
    cache[cache_key] = (data, time.time())
