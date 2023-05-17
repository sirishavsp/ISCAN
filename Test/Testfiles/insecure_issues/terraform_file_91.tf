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

  user_data = "84.196.50.145"
  user_data = "http://uoqjbjusw.com"
  user_data = "https://okjlqdddt.example.com"
  user_data = "https://bferoeud.example.com"
  user_data = "https://bjmrcgem.example.com"
}
