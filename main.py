"""
Phone and Email Search

This program takes text from the clipboard,
finds phone numbers and email addresses,
and copies only those results back to the clipboard.
"""  # This is a docstring explaining what the program does

import re  # Imports Python's regular expression module for pattern matching
import pyperclip  # Imports module to copy from and paste to the system clipboard


# Get text from clipboard that has been copied by me
text = pyperclip.paste()  # Retrieves whatever text is currently on the clipboard and stores it in 'text'


# Phone number pattern
phone_regex = re.compile(r'''  # Compiles the following regex pattern into a reusable object
(                             # Start of outer capturing group (captures the full phone number)
(\d{3}|\(\d{3}\))?            # Optional area code: either 3 digits OR 3 digits inside parentheses
(\s|-|\.)?                    # Optional separator: space, hyphen, or period
\d{3}                         # First 3 digits of the phone number (required)
(\s|-|\.)                     # Separator: space, hyphen, or period (required here)
\d{4}                         # Last 4 digits of the phone number (required)
)                             # End of outer capturing group
''', re.VERBOSE)              # re.VERBOSE allows whitespace and comments inside the regex for readability


# Email pattern
email_regex = re.compile(r'''  # Compiles the following email regex pattern
(                              # Start of capturing group (captures full email)
[a-zA-Z0-9._%+-]+              # Username: one or more allowed characters (letters, digits, ., _, %, +, -)
@                              # Literal @ symbol separating username and domain
[a-zA-Z0-9.-]+                 # Domain name: one or more letters, digits, dots, or hyphens
\.[a-zA-Z]{2,}                 # Dot followed by 2 or more letters like .com, .org
)                              # End of capturing group
''', re.VERBOSE)               # Allows formatting and comments inside regex


# Find matches
phone_matches = []  # Creates an empty list to store found phone numbers

for groups in phone_regex.findall(text):  # Loops through all phone number matches found in 'text'
    phone_matches.append(groups[0])  # Adds only the full match (first element of tuple) to the list

email_matches = email_regex.findall(text)  # Finds all email matches and stores them in a list


# Combine results
all_matches = []  # Creates an empty list to hold both phone and email matches

all_matches.extend(phone_matches)  # Adds each phone number from phone_matches into all_matches
all_matches.extend(email_matches)  # Adds each email from email_matches into all_matches


# Output
if len(all_matches) > 0:  # Checks if at least one phone number or email was found

    results = "\n".join(all_matches)  # Joins all matches into one string separated by newline characters

    pyperclip.copy(results)  # Copies the results string back to the clipboard

    print("Phone numbers and email addresses copied to clipboard:")  # Prints confirmation message
    print(results)  # Prints the found phone numbers and email addresses

else:  # If no matches were found

    print("No phone numbers or email addresses found.")  # Prints message indicating nothing was found