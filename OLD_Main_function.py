import datetime
from datetime import date
import os.path, time
import os

print('Hi')
for maindir, subdirs, fileslist in os.walk(r'F:\Data\Pixel 01-03-20\Download'):
    for singlefile in fileslist:
        # Stores the file name with path
        filename = os.path.join(maindir, singlefile)
        print(filename)
        extn = os.path.splitext(filename)

        # Store time of file modification in string
        x = datetime.datetime.strptime(time.ctime(os.path.getmtime(filename)), "%a %b %d %H:%M:%S %Y").date()
        x = x.strftime("%d-%b-%Y")
        x = x.upper()
        # x = x.strftime("%d-%m-%Y--%b")
        print(x)
        x = str(x)
        x = x.replace(':', '.')

        # Join File name with the date and time string
        x = extn[0] + ' ' + '(' + x + ')'  + extn[1]
        print(x)

        # Rename files
        os.rename(filename, x)

print('done')