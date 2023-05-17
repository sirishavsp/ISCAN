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

  user_data = "4.180.115.97"
  user_data = "74.58.192.28"
  user_data = "http://ctudbsur.com"
  user_data = "12.230.87.12"
  user_data = "142.114.1.49"
  user_data = "https://ptrwgvd.example.com"
  user_data = "https://wjvqrjs.example.com"
  user_data = "https://ismvrjz.example.com"
}
