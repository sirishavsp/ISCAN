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

  user_data = "157.168.91.99"
  user_data = "85.14.128.213"
  user_data = "125.87.125.187"
  user_data = "https://bdaot.example.com"
  user_data = "https://geyvnq.example.com"
  user_data = "https://suyvhltrp.example.com"
  user_data = "https://wmjvmpdmx.example.com"
}
