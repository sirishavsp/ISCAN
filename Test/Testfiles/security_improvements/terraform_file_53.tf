
# Terraform file 53

variable "region" {
    type    = "string"
    default = "us-west-2"
}


resource "aws_instance" "example" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"

    tags = {
        Name        = "example-instance"
        Environment = "production"
    }
}



resource "aws_instance" "example" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"

    tags = {
        Name        = "example-instance"
        Environment = "production"
    }
}



resource "aws_instance" "example" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"

    tags = {
        Name        = "example-instance"
        Environment = "production"
    }
}



resource "aws_instance" "example" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"

    tags = {
        Name        = "example-instance"
        Environment = "production"
    }
}


# Trade call first seven officer each live let.
# Very travel admit member spring.
# Leave begin guess hear blood drop.


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


# Loss stay them seem.
# Mind about enjoy executive get.