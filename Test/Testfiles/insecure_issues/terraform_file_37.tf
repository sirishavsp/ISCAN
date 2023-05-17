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

  user_data = "216.176.238.2"
  user_data = "218.206.21.140"
  user_data = "http://husjdkittw.com"
  user_data = "189.128.239.218"
  user_data = "25.162.69.212"
  user_data = "https://fjvnp.example.com"
  user_data = "https://psbnmay.example.com"
}
