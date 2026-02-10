from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

# A simple retry mechanism to handle eventual consistency or transient issues.
@retry(
    stop=stop_after_attempt(3), # retry up to 3 times
    wait=wait_fixed(1), # wait 1 second between retries
    retry=retry_if_exception_type(Exception), # retry on any exception
    reraise=True # re-raise the last exception if all retries fail
)
def retryable(fn):
    return fn()
