import os
import random
from pathlib import Path

def generate_test_files(num_files=100):
    # Create a directory for test files
    Path("insecure_permissions").mkdir(parents=True, exist_ok=True)

    # AWS AMI IDs and instance types for random selection
    ami_ids = ['ami-0abcdef1234567890', 'ami-1abcdef1234567890', 'ami-2abcdef1234567890']
    instance_types = ['t2.micro', 't2.small', 't2.medium']

    for i in range(num_files):
        # Randomly select permissions in the range from 0 (no permissions) to 7 (full permissions)
        user_perm = random.randint(0, 7)
        group_perm = random.randint(0, 7)
        other_perm = random.randint(0, 7)

        # Create file with the chosen permissions
        file_name = f"insecure_permissions/test_file_{i}.tf"
        with open(file_name, "w") as f:
            # Write an AWS instance resource with random ami and instance_type
            f.write(f'resource "aws_instance" "example_{i}" {{\n  ami           = "{random.choice(ami_ids)}"\n  instance_type = "{random.choice(instance_types)}"\n  vpc_security_group_ids = ["sg-0123456789abcdef0"]\n  subnet_id              = "subnet-0123456789abcdef0"\n  user_data              = "#!/bin/bash\\necho Hello, world!"\n}}\n')

            # Write an AWS security group resource
            f.write(f'resource "aws_security_group" "example_{i}" {{\n  name        = "example"\n  description = "Example security group"\n  vpc_id      = "vpc-0123456789abcdef0"\n\n  ingress {{\n    from_port   = 22\n    to_port     = 22\n    protocol    = "tcp"\n    cidr_blocks = ["0.0.0.0/0"]\n  }}\n}}\n')

        # Set permissions for the file
        os.chmod(file_name, int(f"{user_perm}{group_perm}{other_perm}", 8))

generate_test_files()
