
import pytest
class error(Exception):
    def __init__(self,message='Value not in range'):
        self.message=message
        super().__init__(self,message)



