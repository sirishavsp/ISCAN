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

  user_data = "163.111.244.227"
  user_data = "61.4.38.67"
  user_data = "https://zegwttn.example.com"
  user_data = "https://jkebjnwtvt.example.com"
  user_data = "https://gkrbp.example.com"
  user_data = "https://frmqivxkgq.example.com"
  user_data = "https://ywzuxlamk.example.com"
}
