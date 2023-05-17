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

  user_data = "http://nwyhnoa.com"
  user_data = "https://tukpuxzu.example.com"
  user_data = "https://gxrucdicgm.example.com"
  user_data = "https://rxmuufgvy.example.com"
  user_data = "https://fotexc.example.com"
  user_data = "https://kznle.example.com"
}
