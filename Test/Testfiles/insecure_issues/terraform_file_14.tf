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

  user_data = "103.30.35.102"
  user_data = "228.141.60.38"
  user_data = "127.123.237.178"
  user_data = "https://zxvkyot.example.com"
  user_data = "https://nawxtgw.example.com"
  user_data = "https://tzkuays.example.com"
  user_data = "https://hkwwzuko.example.com"
}
