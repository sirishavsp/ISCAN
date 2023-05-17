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

  user_data = "http://cdhfo.com"
  user_data = "http://whfvsbou.com"
  user_data = "51.1.180.73"
  user_data = "https://cuevcvkhdr.example.com"
  user_data = "https://lvzzp.example.com"
}
