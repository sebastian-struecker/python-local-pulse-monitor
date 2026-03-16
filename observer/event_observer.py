from watchdog.observers import Observer


def create_observer(handler, path: str = ".") -> Observer:
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    return observer
