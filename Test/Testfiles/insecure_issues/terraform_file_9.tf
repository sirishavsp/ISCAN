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

  user_data = "http://eyiqxftcic.com"
  user_data = "https://gpcul.example.com"
  user_data = "https://fpxeynl.example.com"
  user_data = "https://nbzksrsz.example.com"
}
