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

  user_data = "173.219.145.236"
  user_data = "160.43.146.11"
  user_data = "0.3.220.63"
  user_data = "http://ydzwckemfz.com"
  user_data = "216.69.215.7"
  user_data = "https://lljlwsb.example.com"
  user_data = "https://xrmriyckcl.example.com"
  user_data = "https://tctpzhr.example.com"
  user_data = "https://yykvakyl.example.com"
}
