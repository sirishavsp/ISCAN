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

{generate_resources(fake, i % 2 == 0)}

"""

        comments = generate_similar_comments(fake)
        resource_index = random.randint(0, len(comments)-1)

        resource_blocks = generate_resources(fake, i % 2 != 0)
        file_contents += place_comments_near_resources(comments[:resource_index], resource_blocks)
        file_contents += place_comments_near_resources(comments[resource_index:], resource_blocks)

        directory = "duplicate_code"
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, f"terraform_file_{i + 1}.tf")
        with open(file_path, "w") as f:
            f.write(file_contents)

        print(f"Generated Terraform file: {file_path}")

def generate_resources(fake, different_configs):
    # Generate resource blocks with variations
    resources = [
        '''
resource "aws_instance" "example" {{
    ami           = "{fake.uuid4()}"
    instance_type = "{fake.word()}"
    subnet_id     = "{fake.uuid4()}"

    tags = {{
        Name        = "{fake.word()}"
        Environment = "{fake.word()}"
    }}
}}
''',
        '''
resource "aws_security_group" "example" {{
    name        = "{fake.word()}"
    description = "{fake.sentence()}"

    ingress {{
        from_port   = {random.randint(1, 65535)}
        to_port     = {random.randint(1, 65535)}
        protocol    = "{fake.word()}"
        cidr_blocks = ["0.0.0.0/0"]
    }}

    ingress {{
        from_port   = {random.randint(1, 65535)}
        to_port     = {random.randint(1, 65535)}
        protocol    = "{fake.word()}"
        cidr_blocks = ["0.0.0.0/0"]
    }}

    egress {{
        from_port   = {random.randint(1, 65535)}
        to_port     = {random.randint(1, 65535)}
        protocol    = "{fake.word()}"
        cidr_blocks = ["0.0.0.0/0"]
    }}
}}
'''
    ]

    # Randomly select and repeat resource blocks
    num_resources = random.randint(2, 5)
    if different_configs:
        selected_resources = random.choices(resources, k=num_resources)
    else:
        selected_resource = random.choice(resources)
        selected_resources = [selected_resource] * num_resources
    return selected_resources

def place_comments_near_resources(comments, resource_blocks):
    result = ""
    for resource, comment in zip(resource_blocks, comments):
        result += comment + "\n"
        result += resource + "\n\n"
    return result

def generate_similar_comments(fake):
    # Generate similar comments
    comments = []
    for _ in range(5):
        comment = fake.paragraph(nb_sentences=1)
        comments.append(f"# {comment}")

    return comments

generate_terraform_files(100)
