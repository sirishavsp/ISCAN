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

  user_data = "175.52.21.41"
  user_data = "154.119.80.35"
  user_data = "125.180.233.228"
  user_data = "http://jissdw.com"
  user_data = "http://lcnlri.com"
  user_data = "https://ipbkuxc.example.com"
}
