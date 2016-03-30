#E-Book User Count

This Python script identifies the maximum number of simultaneous users for ebrary and EBSCO e-books.

##Requirements
- [Python](https://www.python.org/downloads/) must be installed.
- After installing Python, install Selenium by typing `pip install -U selenium` into the command line.
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) also needs to be installed.
- This script has been tested on Windows 8.1 with Python 3.5.1, Selenium 2.53.1, and Firefox 45.0.1.

##Usage
The input file must be a .csv with the e-book URL in the final (rightmost) column. It should be located in the same directory as EbookUserCount.py. The output file is also a .csv file containing all the data from the input file with the addition of another column headed USERS. The script checks each e-book page for text indicating the number of users, which is added to the USERS column of the output file. If the number of users cannot be determined, the output in the USERS column will say "check".

To run the script from the command line, first move to the directory where EbookUserCount.py is located. Then type the following and hit Enter:

`python EbookUserCount.py input.csv output.csv`

where 

- `input.csv` is the name of your input file, and
- `output.csv` is the name of the output file that will be created.

##Author
Rebecca French

##License
This script is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.