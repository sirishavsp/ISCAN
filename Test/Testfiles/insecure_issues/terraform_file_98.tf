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

  user_data = "44.42.71.240"
  user_data = "66.213.190.192"
  user_data = "http://sprigm.com"
  user_data = "http://dcmfrgcrlu.com"
  user_data = "https://hzxwrlj.example.com"
}
