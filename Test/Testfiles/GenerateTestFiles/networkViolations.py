import os
import random
import string
from pathlib import Path

# Define secure and insecure protocols
secure_protocols = ['https']
insecure_protocols = ['http', 'ftp', 'telnet', 'smtp', 'pop3', 'imap']

# AWS AMI IDs and instance types for random selection
ami_ids = ['ami-0abcdef1234567890', 'ami-1abcdef1234567890', 'ami-2abcdef1234567890']
instance_types = ['t2.micro', 't2.small', 't2.medium']

def generate_terraform_file(file_path):
    terraform_file = ""

    # Generate AWS instance resources with a mix of secure and insecure user_data
    for i in range(50):
        protocol = random.choice(insecure_protocols if i % 2 == 0 else secure_protocols)
        random_chars = "".join(random.choices(string.ascii_lowercase, k=10))
        url = f'{protocol}://{random_chars}.example.com'
        terraform_file += f'resource "aws_instance" "example_{i}" {{\n  ami           = "{random.choice(ami_ids)}"\n  instance_type = "{random.choice(instance_types)}"\n  vpc_security_group_ids = ["sg-0123456789abcdef0"]\n  subnet_id              = "subnet-0123456789abcdef0"\n  user_data              = "{url}"\n}}\n\n'

    with open(file_path, "w") as f:
        f.write(terraform_file)

# Create a directory for the generated files
directory = "network_violations"
Path(directory).mkdir(parents=True, exist_ok=True)

# Generate 100 Terraform files with different combinations of violations
for i in range(100):
    file_path = os.path.join(directory, f"terraform_file_{i}.tf")
    generate_terraform_file(file_path)
