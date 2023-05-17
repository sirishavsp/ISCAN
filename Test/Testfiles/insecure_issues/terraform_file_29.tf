terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.58.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
  profile = "my-profile"
}

resource "aws_instance" "example" {
  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t2.micro"

  user_data = "152.241.69.157"
  user_data = "192.152.145.119"
  user_data = "68.57.160.23"
  user_data = "https://bkdkicigb.example.com"
  user_data = "https://vvevoy.example.com"
  user_data = "https://plrcwhi.example.com"
}
