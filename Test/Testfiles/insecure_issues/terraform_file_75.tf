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

  user_data = "118.174.30.101"
  user_data = "111.28.125.74"
  user_data = "http://xwmrsyugw.com"
  user_data = "https://etysvy.example.com"
  user_data = "https://zjlxzdw.example.com"
  user_data = "https://sbeoml.example.com"
}
