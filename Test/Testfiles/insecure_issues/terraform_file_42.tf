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

  user_data = "19.180.221.27"
  user_data = "http://yxhltey.com"
  user_data = "163.185.10.111"
  user_data = "http://nizmgit.com"
  user_data = "http://rjioryy.com"
  user_data = "https://ibswzena.example.com"
}
