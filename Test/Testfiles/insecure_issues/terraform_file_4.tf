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

  user_data = "http://vvriioior.com"
  user_data = "210.0.71.106"
  user_data = "121.63.43.199"
  user_data = "https://gwbpssqr.example.com"
  user_data = "https://syfion.example.com"
  user_data = "https://rykkoaqxcr.example.com"
  user_data = "https://tmuqfpwu.example.com"
}
