# TODO: Import Methods
from converter import Converter

# TODO: Create Object => MAIN_OBJECT
MAIN_OBJECT = Converter()

while True:
    user_command = input("REST >>> ")
    if user_command == "C":
        MAIN_OBJECT.cc()


