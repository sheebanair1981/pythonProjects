import os
import datetime

def file_date(filename) -> object:
    # Create the file in the current directory
    with open(filename, 'w') as f1:
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    time_readable = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{}".format(time_readable.strftime("%Y-%m-%d"))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
