import os
import random
from faker import Faker

def generate_terraform_files(num_files):
    fake = Faker()

    for i in range(num_files):
        file_contents = f"""
# Terraform file {i + 1}

variable "region" {{
    type    = "string"
    default = "us-west-2"
}}

{generate_resources(fake)}

"""

        comments = generate_similar_comments(fake)
        resource_index = random.randint(0, len(comments)-1)

        file_contents += "\n".join(comments[:resource_index])
        file_contents += "\n\n"
        file_contents += generate_resources(fake)
        file_contents += "\n\n"
        file_contents += "\n".join(comments[resource_index:])

        directory = "security_improvements"
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, f"terraform_file_{i + 1}.tf")
        with open(file_path, "w") as f:
            f.write(file_contents)

        print(f"Generated Terraform file: {file_path}")

def generate_resources(fake):
    # Generate resource blocks with variations
    resources = [
        '''
resource "aws_instance" "example" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"

    tags = {
        Name        = "example-instance"
        Environment = "production"
    }
}
''',
        '''
resource "aws_security_group" "example" {
    name        = "example-security-group"
    description = "Example security group"

    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
'''
    ]

    # Randomly select and repeat resource blocks
    num_resources = random.randint(2, 5)
    selected_resources = random.choices(resources, k=num_resources)
    return "\n\n".join(selected_resources)

def generate_similar_comments(fake):
    # Generate similar comments
    comments = []
    for _ in range(5):
        comment = fake.paragraph(nb_sentences=1)
        comments.append(f"# {comment}")

    return comments

generate_terraform_files(100)
