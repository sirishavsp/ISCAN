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

  user_data = "185.163.183.164"
  user_data = "128.87.104.211"
  user_data = "http://avchbvimd.com"
  user_data = "http://tjppoo.com"
  user_data = "https://vadinbzf.example.com"
  user_data = "https://dgjbwhn.example.com"
}
