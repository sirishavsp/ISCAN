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

  user_data = "144.88.119.235"
  user_data = "181.30.220.23"
  user_data = "https://crsnl.example.com"
  user_data = "https://freegd.example.com"
  user_data = "https://mtufkuk.example.com"
  user_data = "https://wofcbi.example.com"
}
