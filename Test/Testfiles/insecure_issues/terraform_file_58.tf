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

  user_data = "http://ukjrm.com"
  user_data = "http://lpuighzz.com"
  user_data = "218.193.70.143"
  user_data = "https://syndogb.example.com"
}
