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

  user_data = "http://ijqnvh.com"
  user_data = "http://avvtl.com"
  user_data = "55.20.186.81"
  user_data = "https://bdhmjl.example.com"
}
