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

  user_data = "http://xcbsux.com"
  user_data = "30.16.220.186"
  user_data = "https://rslnz.example.com"
  user_data = "https://xjhdk.example.com"
}
