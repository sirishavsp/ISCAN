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

  user_data = "http://jwknzpq.com"
  user_data = "http://yetpvtbipj.com"
  user_data = "56.56.192.157"
  user_data = "https://onnrudi.example.com"
  user_data = "https://qwljzhrkd.example.com"
  user_data = "https://ntldwgjnq.example.com"
  user_data = "https://aedvg.example.com"
  user_data = "https://tiwpgf.example.com"
}
