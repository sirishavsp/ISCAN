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

  user_data = "71.250.152.250"
  user_data = "http://wzejt.com"
  user_data = "http://jjyaojqe.com"
  user_data = "https://lzzwypzki.example.com"
  user_data = "https://qqcjju.example.com"
}
