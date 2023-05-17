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

  user_data = "7.91.138.244"
  user_data = "http://plgnkuxe.com"
  user_data = "http://ouxfdxsmfi.com"
  user_data = "156.46.134.2"
  user_data = "122.196.236.13"
  user_data = "https://iekow.example.com"
  user_data = "https://rsonguhywu.example.com"
  user_data = "https://bnzbt.example.com"
}
