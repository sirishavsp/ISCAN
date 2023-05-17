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

  user_data = "208.119.153.154"
  user_data = "https://jpepfxp.example.com"
  user_data = "https://padzq.example.com"
  user_data = "https://nxctq.example.com"
  user_data = "https://yrnar.example.com"
  user_data = "https://pihhtbtq.example.com"
}
