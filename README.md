# HIBP

This python script uses the Have I Been Pwned API to check if a list of emails has been involved in any data breaches. It also checks if any of the breaches contained a password compromise.

## Prerequisites

* Python 3.6 or higher
* A Have I Been Pwned API key. You can sign up for a paid account at https://haveibeenpwned.com/API/Key

## Getting Started

1.  Clone or download this repository
2.  Navigate to the directory where you cloned or downloaded the repository
3.  Open hibp.py in a text editor
4.  Replace (YOUR API KEY HERE) with your Have I Been Pwned API key
5.  Run the script using python hibp.py

## Input File

* emails.txt: This is the file containing the list of emails to check. Each email must be on its own line.

## Output

The script will output a list of emails and number of breaches. If a breach contained a password compromise, the name of the breach and date of breach will be outputted.

## Contact

If you have any questions or issues with the script, please open an issue in this repository.
