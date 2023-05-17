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

  user_data = "59.50.199.79"
  user_data = "http://jyrcjd.com"
  user_data = "244.174.185.90"
  user_data = "225.111.42.21"
  user_data = "https://kfcgtiie.example.com"
  user_data = "https://rboxvq.example.com"
  user_data = "https://nyaotcobs.example.com"
}
