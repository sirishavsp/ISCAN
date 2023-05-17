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

  user_data = "http://arxleqonw.com"
  user_data = "http://azneck.com"
  user_data = "142.199.39.87"
  user_data = "http://zmwueyovk.com"
  user_data = "https://apbtzjrmxe.example.com"
  user_data = "https://ztmiqwzwjg.example.com"
  user_data = "https://lfcjagwcu.example.com"
  user_data = "https://szacroyly.example.com"
}
