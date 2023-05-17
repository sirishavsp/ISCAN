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

  user_data = "45.48.224.69"
  user_data = "http://nzxmdwbr.com"
  user_data = "103.122.5.39"
  user_data = "https://rcfnybgl.example.com"
  user_data = "https://kcirw.example.com"
  user_data = "https://abkhhn.example.com"
}
