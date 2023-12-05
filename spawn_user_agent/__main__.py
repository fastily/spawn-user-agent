"""Main driver, helpful for testing/debugging purposes."""

from .user_agent import SpawnUserAgent

if __name__ == "__main__":
    for s in SpawnUserAgent.generate_all():
        print(s)
