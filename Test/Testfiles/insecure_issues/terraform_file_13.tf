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

  user_data = "60.99.141.200"
  user_data = "http://kchfc.com"
  user_data = "60.225.72.158"
  user_data = "https://qjgynef.example.com"
  user_data = "https://fvsucmh.example.com"
  user_data = "https://uhwibgsmq.example.com"
  user_data = "https://dvjyd.example.com"
}
