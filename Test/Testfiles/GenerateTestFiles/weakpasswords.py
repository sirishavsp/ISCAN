import random
import string
import os

secret_types = ["password", "pwd", "secret", "access_key", "secret_key", "private_key", "ssh_key"]

aws_resources = [
    "aws_instance",
    "aws_s3_bucket",
    "aws_db_instance",
    "aws_security_group",
    "aws_vpc"
]

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_tf_file(file_name):
    resource_type = random.choice(aws_resources)
    resource_name = random_string()
    secret_type = random.choice(secret_types)
    secret_value = random_string()

    with open(file_name, "w") as f:
        # Variables block
        f.write(f'variable "{secret_type}" {{\n')
        f.write(f'  description = "The {secret_type}"\n')
        f.write(f'  type = string\n')
        f.write('}\n\n')

        # Resources block
        f.write(f'resource "{resource_type}" "{resource_name}" {{\n')
        f.write(f'  {secret_type} = var.{secret_type}\n')
        f.write('}\n\n')

        # Outputs block
        f.write(f'output "{secret_type}" {{\n')
        f.write(f'  value = {resource_type}.{resource_name}.{secret_type}\n')
        f.write('}\n\n')

        # Module block
        f.write('module "secure_module" {\n')
        f.write(f'  source = "./modules/{random_string()}"\n')
        f.write(f'  {secret_type} = var.{secret_type}\n')
        f.write('}\n')

os.makedirs("weak_passwords", exist_ok=True)
for i in range(1, 101):
    file_name = f"weak_passwords/test_{i}.tf"
    generate_tf_file(file_name)
