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

  user_data = "http://ieqrz.com"
  user_data = "60.35.206.176"
  user_data = "19.5.178.240"
  user_data = "55.189.106.142"
  user_data = "https://slbvs.example.com"
  user_data = "https://hfdvnu.example.com"
  user_data = "https://skmckbd.example.com"
  user_data = "https://fgcdmxi.example.com"
}
