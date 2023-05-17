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

  user_data = "100.14.78.136"
  user_data = "http://aiatuuiknn.com"
  user_data = "133.32.161.75"
  user_data = "http://gkjcutq.com"
  user_data = "https://grsanmej.example.com"
  user_data = "https://vwnlfqrwtw.example.com"
  user_data = "https://nimtezalws.example.com"
  user_data = "https://wxmtcqgsjr.example.com"
}
