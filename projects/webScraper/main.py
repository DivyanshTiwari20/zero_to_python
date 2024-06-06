import requests
import random
from itertools import cycle
import logging
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import re
from urllib.parse import unquote
from selenium import webdriver
import os
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException

MAX_RETRIES = 3

def make_request_with_retries(url, session):
    retries = Retry(total=MAX_RETRIES, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))

    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            return response
        except Exception as e:
            logging.error(f"Request failed: {e}")
            time.sleep(5)  # Delay before retrying

    raise Exception("Request failed after maximum retries")

def rotate_proxies(proxies):
    proxy_pool = cycle(proxies)
    return proxy_pool

def make_request_with_rotation(url, proxy_pool, session):
    proxy = next(proxy_pool)
    response = session.get(url, proxies={"http": proxy, "https": proxy})
    return response

def scrape_phone_numbers(page_source):
    return re.findall(r'\b(?:\+\d{1,2}\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', page_source)

def scrape_emails(page_source):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', page_source)

if __name__ == "__main__":
    # Example proxy list (replace with your proxies)
    proxies = [
        "http://103.155.217.1:41317",
        "http://47.91.56.120:8080",
        # Add more proxies as needed
    ]

    target_url = input("Enter the URL of the website: ")

    # Create a session for retries
    session = requests.Session()

    # Rotate proxies
    proxy_pool = rotate_proxies(proxies)

    try:
        # Use headless mode to hide the browser window
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        # Remove the executable_path argument here
        driver = webdriver.Chrome(options=options)
        driver.get(target_url)

        # Wait for the page to load (you can adjust the sleep duration if needed)
        time.sleep(5)

        # Get the page source after the wait
        page_source = driver.page_source

        # Initialize list_of_links
        list_of_links = []

        # Extract links from the rendered page
        for re_match in re.finditer(r'https?://[^\s<>"]+|www\.[^\s<>"]+', page_source):
            if re_match.group() not in list_of_links:
                list_of_links.append(re_match.group())

        # Filter out non-hyperlink items (e.g., SVG images)
        filtered_links = [link for link in list_of_links if not link.startswith('data:image/svg+xml')]

        # Extract phone numbers and emails
        phone_numbers = scrape_phone_numbers(page_source)
        emails = scrape_emails(page_source)

        # Prompt user for file name, quantity, and file format
        folder_name = "extracted_files"
        folder_path = os.path.join(os.getcwd(), folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = input("Enter the desired file name (without extension): ")
        num_links_to_extract = input("How many links do you want to extract? Press enter for all links: ")
        num_emails_to_extract = input("How many emails do you want to extract? Press enter for all emails: ")
        num_phone_numbers_to_extract = input("How many phone numbers do you want to extract? Press enter for all phone numbers: ")

        try:
            num_links_to_extract = int(num_links_to_extract) if num_links_to_extract else len(filtered_links)
            num_emails_to_extract = int(num_emails_to_extract) if num_emails_to_extract else len(emails)
            num_phone_numbers_to_extract = int(num_phone_numbers_to_extract) if num_phone_numbers_to_extract else len(phone_numbers)

            if num_links_to_extract <= 0 or num_emails_to_extract <= 0 or num_phone_numbers_to_extract <= 0:
                print("Please enter valid numbers greater than 0.")
            else:
                file_format = input("Enter the desired file format (e.g., txt, pdf, docx, xlsx, json, csv): ").lower()

                file_path = os.path.join(folder_path, f"{file_name}.{file_format}")

                if os.path.exists(file_path):
                    user_input = input(f"A file with the name '{file_name}.{file_format}' already exists. Do you want to replace it? (yes/no): ").lower()
                    if user_input == 'no':
                        file_name = input("Enter a new name for the file (without extension): ")
                        file_path = os.path.join(folder_path, f"{file_name}.{file_format}")

                with open(file_path, "w") as file:
                    for i, link in enumerate(filtered_links[:num_links_to_extract]):
                        # Check if the link is URL-encoded and decode it
                        if '%' in link:
                            decoded_link = unquote(link)
                            file.write(f'{i + 1}: {decoded_link}\n')
                        else:
                            file.write(f'{i + 1}: {link}\n')

                    for i, email in enumerate(emails[:num_emails_to_extract]):
                        file.write(f'Email {i + 1}: {email}\n')

                    for i, phone_number in enumerate(phone_numbers[:num_phone_numbers_to_extract]):
                        file.write(f'Phone Number {i + 1}: {phone_number}\n')

                if num_links_to_extract < len(filtered_links):
                    print(f"\nScraping completed successfully. Extracted {num_links_to_extract} links out of {len(filtered_links)}.")
                else:
                    print(f"\nScraping completed successfully. Extracted {num_links_to_extract} links.")
                
                if num_emails_to_extract < len(emails):
                    print(f"Extracted {num_emails_to_extract} emails out of {len(emails)}.")
                else:
                    print(f"Extracted {num_emails_to_extract} emails.")
                
                if num_phone_numbers_to_extract < len(phone_numbers):
                    print(f"Extracted {num_phone_numbers_to_extract} phone numbers out of {len(phone_numbers)}.")
                else:
                    print(f"Extracted {num_phone_numbers_to_extract} phone numbers.")

        except WebDriverException as e:
            print(f"WebDriverException: {e}")
        except TimeoutException as e:
            print(f"TimeoutException: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    finally:
        # Close the WebDriver, even if an exception occurs
        driver.quit()
