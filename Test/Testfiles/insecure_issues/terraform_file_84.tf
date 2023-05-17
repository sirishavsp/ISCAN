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

  user_data = "171.139.112.119"
  user_data = "https://koclidzf.example.com"
  user_data = "https://zoxjrx.example.com"
  user_data = "https://ohbgrrqrwf.example.com"
  user_data = "https://ojdeze.example.com"
  user_data = "https://twoqzwm.example.com"
}
