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

  user_data = "http://lwsde.com"
  user_data = "http://prhclima.com"
  user_data = "134.76.33.175"
  user_data = "https://tssfpqq.example.com"
  user_data = "https://vcqakkddbb.example.com"
  user_data = "https://zgdhfhz.example.com"
  user_data = "https://aauvwkkun.example.com"
}
