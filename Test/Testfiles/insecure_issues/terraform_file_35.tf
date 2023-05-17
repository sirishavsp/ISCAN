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

  user_data = "112.19.181.78"
  user_data = "http://ubkksanh.com"
  user_data = "https://assbogv.example.com"
  user_data = "https://yienc.example.com"
  user_data = "https://zowox.example.com"
  user_data = "https://fonxrkfici.example.com"
}
