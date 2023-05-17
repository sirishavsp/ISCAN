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

  user_data = "http://atvgqx.com"
  user_data = "http://kgbep.com"
  user_data = "242.95.0.228"
  user_data = "http://svwdk.com"
  user_data = "http://zsgawv.com"
  user_data = "https://jhjqv.example.com"
  user_data = "https://tazssvja.example.com"
  user_data = "https://opaocyobkm.example.com"
  user_data = "https://pdbedrl.example.com"
  user_data = "https://rnwrrlfw.example.com"
}
