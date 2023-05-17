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

  user_data = "164.36.193.114"
  user_data = "https://vqzxlz.example.com"
  user_data = "https://gxwwuppc.example.com"
  user_data = "https://innjklwmba.example.com"
  user_data = "https://ntsgdot.example.com"
}
