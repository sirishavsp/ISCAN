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

  user_data = "104.81.34.143"
  user_data = "http://vrbmwpkxke.com"
  user_data = "145.217.60.139"
  user_data = "https://bxiwojp.example.com"
  user_data = "https://zaryrlo.example.com"
}
