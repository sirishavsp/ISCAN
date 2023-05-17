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

  user_data = "182.155.59.120"
  user_data = "http://qdihp.com"
  user_data = "http://llsklqub.com"
  user_data = "http://nkrjcqabb.com"
  user_data = "178.226.236.184"
  user_data = "https://tqqdfqrhe.example.com"
}
