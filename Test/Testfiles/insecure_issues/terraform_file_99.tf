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

  user_data = "http://nwdzzrnh.com"
  user_data = "27.122.197.235"
  user_data = "https://dynabrrvw.example.com"
  user_data = "https://vdois.example.com"
  user_data = "https://yqbfoxvi.example.com"
  user_data = "https://mqrteanr.example.com"
  user_data = "https://ewettzbaj.example.com"
}
