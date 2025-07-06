# Command Processing Module

class CommandProcessorError(Exception):
    ''' Base class for exceptions '''
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class CommandProcessor:

    def __init__(self ,command_methods: dict, command_length:int = 1) -> None:
        ''' 
            Receives a dictionary for the commands formed with 1 character and the callable method,
            and the length of the command string as an integer number(all commands must have this length).
            Example of the command string:
            {"P":print, "S":sum, "E":eval}
            Returns an instance of a command processor that can route a message to those methods.
        '''
        self.command_methods = command_methods
        self.command_length = command_length
    
    def route(self, message: str):
        '''
            Receives a message with its first character being the command expected to be interpreted,
            and the rest of the string as the data that will be provided as argument to the method called.
        '''
        command = message[:self.command_length]
        data = message[self.command_length:]
        # Possible improvement, receive multiple arguments
        try:
            res = self.command_methods[command](data)
            return res
        except Exception as e:
            return (f"Error processing request: {e}")
