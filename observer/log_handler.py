from watchdog.events import FileSystemEventHandler, FileSystemEvent


class LogHandler(FileSystemEventHandler):
    def __init__(self, on_event_callback):
        self.on_event_callback = on_event_callback

    def on_any_event(self, event: FileSystemEvent) -> None:
        self.on_event_callback(event)
