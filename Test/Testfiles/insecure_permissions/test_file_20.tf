resource "aws_instance" "example_20" {
  ami           = "ami-2abcdef1234567890"
  instance_type = "t2.medium"
  vpc_security_group_ids = ["sg-0123456789abcdef0"]
  subnet_id              = "subnet-0123456789abcdef0"
  user_data              = "#!/bin/bash\necho Hello, world!"
}
resource "aws_security_group" "example_20" {
  name        = "example"
  description = "Example security group"
  vpc_id      = "vpc-0123456789abcdef0"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
