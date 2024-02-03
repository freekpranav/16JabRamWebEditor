#!/usr/bin/python3
import urllib.request

url = input("Enter the URL: ")

try:
    response = urllib.request.urlopen(url)
    s = response.read().decode('utf-8')  # Decode the bytes to string using UTF-8
    print(s)
except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")