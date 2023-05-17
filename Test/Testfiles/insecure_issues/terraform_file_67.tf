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

  user_data = "http://sdaugh.com"
  user_data = "http://zscuzfx.com"
  user_data = "http://dhnbxdan.com"
  user_data = "http://gmbyj.com"
  user_data = "http://kggjgcewig.com"
  user_data = "https://ukvyltbj.example.com"
  user_data = "https://jbheurgozz.example.com"
  user_data = "https://pvnng.example.com"
}
