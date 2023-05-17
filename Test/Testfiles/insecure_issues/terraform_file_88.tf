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

  user_data = "207.25.178.228"
  user_data = "http://ozrrrbp.com"
  user_data = "146.2.38.25"
  user_data = "158.180.99.93"
  user_data = "https://sdsukvbp.example.com"
  user_data = "https://tobqy.example.com"
  user_data = "https://sovmb.example.com"
  user_data = "https://eamshhcut.example.com"
  user_data = "https://fwdipae.example.com"
}
