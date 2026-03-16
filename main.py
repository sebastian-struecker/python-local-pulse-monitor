import time

from watchdog.events import FileSystemEvent

from observer import event_observer
from observer.log_handler import LogHandler


def on_log_handler_event(event: FileSystemEvent):
    print(event)


def main():
    log_handler = LogHandler(on_log_handler_event)
    observer = event_observer.create_observer(log_handler, "./logs")
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
