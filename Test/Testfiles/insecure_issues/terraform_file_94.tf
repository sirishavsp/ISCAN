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

  user_data = "90.109.115.167"
  user_data = "79.177.97.22"
  user_data = "http://bmvkjnkg.com"
  user_data = "https://bnhey.example.com"
  user_data = "https://gmedzdlc.example.com"
  user_data = "https://pyodii.example.com"
}
