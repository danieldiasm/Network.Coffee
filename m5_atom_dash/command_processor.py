# Command Processing Module

class CommandProcessorError(Exception):
    ''' Base class for exceptions '''
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class CommandProcessor:

    def __init__(self, command_methods: dict) -> None:
        self.command_methods = command_methods
    
    def route(self, message: str):
        command = message[:1]
        data = message[1:]

        try:
            self.command_methods[command](data)
            return None
        except Exception as e:
            return (f"Error processing request: {e}")
