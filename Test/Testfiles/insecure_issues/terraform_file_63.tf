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

  user_data = "http://xqtvlssrie.com"
  user_data = "http://hglsznz.com"
  user_data = "129.10.243.138"
  user_data = "https://tfkyvftu.example.com"
  user_data = "https://pqypa.example.com"
  user_data = "https://vobdjzikfq.example.com"
  user_data = "https://mgktuhc.example.com"
  user_data = "https://hzprhjknrf.example.com"
}
