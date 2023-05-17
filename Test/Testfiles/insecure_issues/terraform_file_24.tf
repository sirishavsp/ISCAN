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

  user_data = "http://vfdsqedn.com"
  user_data = "191.75.144.212"
  user_data = "http://gnmbfq.com"
  user_data = "http://qqlxon.com"
  user_data = "39.119.71.42"
  user_data = "https://xnset.example.com"
  user_data = "https://iywdhwfii.example.com"
}
