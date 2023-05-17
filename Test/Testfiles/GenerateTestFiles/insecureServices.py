import os
import random
from pathlib import Path

def generate_test_files(num_files=100):
    # Create a directory for test files
    Path("insecure_services").mkdir(parents=True, exist_ok=True)

    # List of secure and insecure services
    services = ['http', 'https', 'ftp', 'telnet']

    # AWS AMI IDs and instance types for random selection
    ami_ids = ['ami-0abcdef1234567890', 'ami-1abcdef1234567890', 'ami-2abcdef1234567890']
    instance_types = ['t2.micro', 't2.small', 't2.medium']

    for i in range(num_files):
        # Create a Terraform file with random resources
        file_name = f"insecure_services/test_file_{i}.tf"
        with open(file_name, "w") as f:
            for _ in range(random.randint(1, 3)):  # Write between 1 and 3 resources
                # Choose a random service, AMI ID, and instance type
                service = random.choice(services)
                ami_id = random.choice(ami_ids)
                instance_type = random.choice(instance_types)

                # Write an aws_vpc and aws_subnet resource
                f.write(f'resource "aws_vpc" "example_vpc" {{\n  cidr_block = "10.0.0.0/16"\n}}\n')
                f.write(f'resource "aws_subnet" "example_subnet" {{\n  vpc_id     = aws_vpc.example_vpc.id\n  cidr_block = "10.0.1.0/24"\n}}\n')

                # Write an aws_instance resource with the chosen service in the user data
                f.write(f'resource "aws_instance" "example" {{\n  ami           = "{ami_id}"\n  instance_type = "{instance_type}"\n  subnet_id     = aws_subnet.example_subnet.id\n  user_data     = "{service}://example.com"\n}}\n')

generate_test_files()
