email_list  = ['a@test.com', 'b@test.com', 'a@test.com','manish@use.com']

unique_emails = list(set(email_list))

output_filename = 'unique_emails.txt'
try:
    with open(output_filename, 'w') as file:
        for email in unique_emails:
            file.write(email + '\n')
    print(f"successfully unique email saved to {output_filename}")
except Exception as e:
    print(f"An error occurred: {e}")