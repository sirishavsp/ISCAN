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

  user_data = "140.176.180.52"
  user_data = "225.218.227.187"
  user_data = "http://ygeqjnaa.com"
  user_data = "https://lqylteih.example.com"
  user_data = "https://ndsvxbg.example.com"
  user_data = "https://ojyehs.example.com"
  user_data = "https://bnasxsjm.example.com"
  user_data = "https://jhrobv.example.com"
}
