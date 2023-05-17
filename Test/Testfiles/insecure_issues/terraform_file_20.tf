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

  user_data = "45.23.181.39"
  user_data = "70.135.113.184"
  user_data = "48.254.172.35"
  user_data = "https://uvkdptks.example.com"
  user_data = "https://xyhbpnkebd.example.com"
  user_data = "https://wqpnnh.example.com"
  user_data = "https://xgogklyo.example.com"
  user_data = "https://vzmobkq.example.com"
}
