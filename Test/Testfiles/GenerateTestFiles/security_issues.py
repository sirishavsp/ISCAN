import os
import random
import string

def generate_complex_tf_files(num_files=100):
    directory = "insecure_issues"
    os.makedirs(directory, exist_ok=True)

    for i in range(num_files):
        file_path = os.path.join(directory, f"terraform_file_{i}.tf")
        with open(file_path, "w") as f:
            f.write('terraform {\n')
            f.write('  required_providers {\n')
            f.write('    aws = {\n')
            f.write('      source  = "hashicorp/aws"\n')
            f.write('      version = "3.58.0"\n')
            f.write('    }\n')
            f.write('  }\n')
            f.write('}\n\n')

            f.write('provider "aws" {\n')
            f.write('  region = "us-west-2"\n')
            f.write('  profile = "my-profile"\n')
            f.write('}\n\n')

            f.write('resource "aws_instance" "example" {\n')
            f.write('  ami           = "ami-0c94855ba95c71c99"\n')
            f.write('  instance_type = "t2.micro"\n\n')

            # Generate random content with hardcoded IPs or domains
            for _ in range(random.randint(1, 5)):
                if random.choice([True, False]):
                    random_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                    f.write(f'  user_data = "{random_ip}"\n')
                else:
                    random_domain = "".join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
                    f.write(f'  user_data = "http://{random_domain}.com"\n')

            # Generate random content without hardcoded IPs or domains
            for _ in range(random.randint(1, 5)):
                random_chars = "".join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
                f.write(f'  user_data = "https://{random_chars}.example.com"\n')

            f.write('}\n')

# Generate 100 complex and realistic Terraform files with increased complexity
generate_complex_tf_files(num_files=100)
