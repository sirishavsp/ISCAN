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

  user_data = "http://bmlko.com"
  user_data = "87.196.183.40"
  user_data = "http://htodjgugu.com"
  user_data = "http://uisrvwlmqq.com"
  user_data = "https://sopmbr.example.com"
  user_data = "https://cijsvk.example.com"
  user_data = "https://ixmch.example.com"
}
