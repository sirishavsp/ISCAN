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

  user_data = "http://irexzcqyaj.com"
  user_data = "12.158.104.248"
  user_data = "33.70.4.87"
  user_data = "https://mysdk.example.com"
  user_data = "https://gkdpcq.example.com"
  user_data = "https://hqvylrkj.example.com"
  user_data = "https://blame.example.com"
}
