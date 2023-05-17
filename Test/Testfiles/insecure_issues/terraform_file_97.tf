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

  user_data = "http://lcuxaeirc.com"
  user_data = "http://kwzhijld.com"
  user_data = "163.170.86.20"
  user_data = "https://anrrvdje.example.com"
  user_data = "https://sovwkw.example.com"
  user_data = "https://xtkemrldxb.example.com"
}
