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

  user_data = "32.11.176.81"
  user_data = "http://ctsxb.com"
  user_data = "http://dmophmm.com"
  user_data = "148.30.121.89"
  user_data = "http://tygjchmbfn.com"
  user_data = "https://eaaua.example.com"
  user_data = "https://xbpqksru.example.com"
}
