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

  user_data = "http://mwcke.com"
  user_data = "161.102.236.129"
  user_data = "155.186.91.220"
  user_data = "207.87.220.160"
  user_data = "http://zpxnak.com"
  user_data = "https://uqpxsrzi.example.com"
}
