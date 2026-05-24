import re
import os

# Create the file automatically if it doesn't exist
if not os.path.exists("contacts.txt"):
    setup_file = open("contacts.txt", "w")
    setup_file.write("lakshmipennada@email.com text here durgapennada@gmail.com")
    setup_file.close()

# 1. Open and read the text inside contacts.txt
file = open("contacts.txt", "r")
content = file.read()
file.close()

# 2. Use a basic formula to find all email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
found_emails = re.findall(email_pattern, content)

# 3. Open a new file to save the results
output_file = open("extracted_emails.txt", "w")

# 4. Write each found email into the new file on a new line
for email in found_emails:
    output_file.write(email + "\n")

output_file.close()

print("Done! Check your extracted_emails.txt file.")