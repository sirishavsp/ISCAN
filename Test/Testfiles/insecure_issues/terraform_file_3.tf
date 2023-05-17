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

  user_data = "52.160.187.25"
  user_data = "65.155.200.72"
  user_data = "https://dpuvsohgpm.example.com"
  user_data = "https://ipgdfhe.example.com"
}
