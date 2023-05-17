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

  user_data = "156.55.164.124"
  user_data = "http://xzcnf.com"
  user_data = "http://bzlrbgj.com"
  user_data = "http://sszrrw.com"
  user_data = "https://rvddpuaq.example.com"
}
