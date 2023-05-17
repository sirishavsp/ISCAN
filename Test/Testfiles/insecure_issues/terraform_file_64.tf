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

  user_data = "http://thvfyw.com"
  user_data = "http://ikuqu.com"
  user_data = "50.212.176.16"
  user_data = "6.221.34.251"
  user_data = "https://bwzxyxaobd.example.com"
  user_data = "https://nkkvwiiyii.example.com"
  user_data = "https://gtjxtcudfq.example.com"
  user_data = "https://xzigcxzi.example.com"
}
