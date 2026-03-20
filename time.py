import time
import threading


# --- 1. Basic sleep ---

def basic_sleep():
    print("Starting basic sleep example...")
    time.sleep(2)  # Pause execution for 2 seconds
    print("2 seconds have passed.")


# --- 2. Countdown timer ---

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"  {i}...")
        time.sleep(1)  # Wait 1 second between each tick
    print("  Go!")


# --- 3. Retry mechanism with sleep ---

def fetch_data(attempt):
    # Simulate a failing operation (succeeds on 3rd attempt)
    if attempt < 3:
        raise ConnectionError("Server not responding.")
    return {"status": "ok", "data": [1, 2, 3]}


def fetch_with_retry(max_retries=5, delay=1.5):
    for attempt in range(1, max_retries + 1):
        try:
            result = fetch_data(attempt)
            print(f"  Success on attempt {attempt}: {result}")
            return result
        except ConnectionError as e:
            print(f"  Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                print(f"  Retrying in {delay} seconds...")
                time.sleep(delay)  # Wait before next retry
    print("  All retries exhausted.")
    return None


# --- 4. Simulating a loading bar ---

def loading_bar(steps=10, step_duration=0.15):
    print("  Loading: [", end="", flush=True)
    for _ in range(steps):
        time.sleep(step_duration)  # Simulate work being done
        print("#", end="", flush=True)
    print("] Done!")


# --- 5. Polling: wait until a condition is met ---

_shared_flag = False


def set_flag_after_delay():
    time.sleep(3)  # Simulate an async event arriving after 3 seconds
    global _shared_flag
    _shared_flag = True


def poll_until_ready(interval=0.5, timeout=10):
    global _shared_flag
    _shared_flag = False

    # Start a background thread that will set the flag
    t = threading.Thread(target=set_flag_after_delay)
    t.start()

    elapsed = 0
    while not _shared_flag:
        if elapsed >= timeout:
            print("  Timed out waiting for flag.")
            return
        print(f"  Not ready yet, checking again in {interval}s...")
        time.sleep(interval)  # Poll at regular intervals
        elapsed += interval

    print(f"  Flag is set! Total wait: ~{elapsed:.1f}s")
    t.join()


# --- 6. Fractional sleep (sub-second precision) ---

def measure_fractional_sleep(duration=0.25):
    start = time.perf_counter()  # Get current time with high precision
    time.sleep(duration)  # Sleep accepts floats for millisecond-level control
    end = time.perf_counter()
    print(f"  Requested: {duration}s | Actual: {end - start:.4f}s")


# --- 7. Timer ---


def timer():
    while True:
        try:
            my_time = int(input("Enter the time in seconds: "))
            if my_time <= 0:
                print("Invalid input!")
                continue
            if my_time > 0:
                break
        except ValueError:
            print("Invalid input!")

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(F"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("TIME'S UP!")


# --- Run all examples ---

if __name__ == "__main__":
    print("\n=== 1. Basic sleep ===")
    basic_sleep()

    print("\n=== 2. Countdown ===")
    countdown(3)

    print("\n=== 3. Retry with sleep ===")
    fetch_with_retry()

    print("\n=== 4. Loading bar ===")
    loading_bar()

    print("\n=== 5. Polling ===")
    poll_until_ready()

    print("\n=== 6. Fractional sleep ===")
    measure_fractional_sleep(0.25)

    print("\n=== 7. Timer ===")
    timer()

    print("")
