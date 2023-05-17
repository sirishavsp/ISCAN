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

  user_data = "246.134.87.74"
  user_data = "http://dvtwhvtfzz.com"
  user_data = "http://ebzasviufw.com"
  user_data = "43.96.156.192"
  user_data = "https://zalagngxl.example.com"
  user_data = "https://ehssl.example.com"
  user_data = "https://vbevjzujju.example.com"
  user_data = "https://ypjesnzpb.example.com"
  user_data = "https://mrogkjgss.example.com"
}
