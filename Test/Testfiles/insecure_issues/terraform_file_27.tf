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

  user_data = "73.183.161.183"
  user_data = "http://ygrazxyqo.com"
  user_data = "https://badotuqvz.example.com"
  user_data = "https://nkvpvltr.example.com"
  user_data = "https://iwvis.example.com"
  user_data = "https://fctywija.example.com"
  user_data = "https://acnbt.example.com"
}
