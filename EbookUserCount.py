#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import sys

def main(input, output):
    browser = webdriver.Firefox()

    outputFile = open(output, 'w')
    writer = csv.writer(outputFile, doublequote=False, lineterminator='\r')

    with open(input, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            result = row
            if 'http' not in row[len(row)-1]:
                result.append('USERS')
                writer.writerow(result)
            else:
                url = row[len(row)-1]
                if 'ebrary' in url:
                    browser.get(url)
                    result.append(browser.find_element_by_xpath(
                        '//div[@id="patron-availability"]/div[@class='
                        '"facultyHolding"]').text)
                    writer.writerow(result)
                elif 'ebscohost' in url:
                    browser.get(url)
                    
                    try:
                        WebDriverWait(browser, 10).until(
                            EC.text_to_be_present_in_element((By.ID,
                            'concurrent_access_level'),'Access'))
                        result.append(browser.find_element_by_id(
                            'concurrent_access_level').text)
                    except TimeoutException:
                        result.append('check')
                    
                    writer.writerow(result)
                else:
                    result.append('check')
                    writer.writerow(result)
    browser.quit()
    outputFile.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])