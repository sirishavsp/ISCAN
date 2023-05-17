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

  user_data = "http://kvjfeu.com"
  user_data = "167.202.167.40"
  user_data = "215.26.241.62"
  user_data = "http://nbjxv.com"
  user_data = "https://fbbgiedaz.example.com"
  user_data = "https://kimghhfvn.example.com"
  user_data = "https://fxctoe.example.com"
  user_data = "https://myvkmurl.example.com"
  user_data = "https://ohuznb.example.com"
}
