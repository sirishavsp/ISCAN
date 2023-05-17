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

  user_data = "http://rbsnp.com"
  user_data = "208.133.166.249"
  user_data = "http://uhjccf.com"
  user_data = "https://rteisl.example.com"
  user_data = "https://ztwzuoqin.example.com"
}
