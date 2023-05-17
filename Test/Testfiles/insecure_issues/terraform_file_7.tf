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

  user_data = "http://uijycnpye.com"
  user_data = "http://owjqmn.com"
  user_data = "http://gclbxon.com"
  user_data = "27.123.193.128"
  user_data = "248.169.94.38"
  user_data = "https://rvilybvgj.example.com"
}
