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

  user_data = "http://ntelxn.com"
  user_data = "174.248.131.44"
  user_data = "https://lbujhh.example.com"
  user_data = "https://ufbbltaevq.example.com"
  user_data = "https://xnweg.example.com"
}
