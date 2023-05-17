
# Terraform file 73

variable "region" {
    type    = "string"
    default = "us-west-2"
}

['\nresource "aws_instance" "example" {{\n    ami           = "{fake.uuid4()}"\n    instance_type = "{fake.word()}"\n    subnet_id     = "{fake.uuid4()}"\n\n    tags = {{\n        Name        = "{fake.word()}"\n        Environment = "{fake.word()}"\n    }}\n}}\n', '\nresource "aws_security_group" "example" {{\n    name        = "{fake.word()}"\n    description = "{fake.sentence()}"\n\n    ingress {{\n        from_port   = {random.randint(1, 65535)}\n        to_port     = {random.randint(1, 65535)}\n        protocol    = "{fake.word()}"\n        cidr_blocks = ["0.0.0.0/0"]\n    }}\n\n    ingress {{\n        from_port   = {random.randint(1, 65535)}\n        to_port     = {random.randint(1, 65535)}\n        protocol    = "{fake.word()}"\n        cidr_blocks = ["0.0.0.0/0"]\n    }}\n\n    egress {{\n        from_port   = {random.randint(1, 65535)}\n        to_port     = {random.randint(1, 65535)}\n        protocol    = "{fake.word()}"\n        cidr_blocks = ["0.0.0.0/0"]\n    }}\n}}\n', '\nresource "aws_security_group" "example" {{\n    name        = "{fake.word()}"\n    description = "{fake.sentence()}"\n\n    ingress {{\n        from_port   = {random.randint(1, 65535)}\n        to_port     = {random.randint(1, 65535)}\n        protocol    = "{fake.word()}"\n        cidr_blocks = ["0.0.0.0/0"]\n    }}\n\n    ingress {{\n        from_port   = {random.randint(1, 65535)}\n        to_port     = {random.randint(1, 65535)}\n        protocol    = "{fake.word()}"\n        cidr_blocks = ["0.0.0.0/0"]\n    }}\n\n    egress {{\n        from_port   = {random.randint(1, 65535)}\n        to_port     = {random.randint(1, 65535)}\n        protocol    = "{fake.word()}"\n        cidr_blocks = ["0.0.0.0/0"]\n    }}\n}}\n', '\nresource "aws_instance" "example" {{\n    ami           = "{fake.uuid4()}"\n    instance_type = "{fake.word()}"\n    subnet_id     = "{fake.uuid4()}"\n\n    tags = {{\n        Name        = "{fake.word()}"\n        Environment = "{fake.word()}"\n    }}\n}}\n']

# Leave speech professor crime.

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


# Talk identify probably.

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


