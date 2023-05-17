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

  user_data = "http://myddki.com"
  user_data = "http://litmttwri.com"
  user_data = "8.64.185.133"
  user_data = "115.227.237.236"
  user_data = "191.140.4.165"
  user_data = "https://refjwsp.example.com"
  user_data = "https://vnxgwn.example.com"
  user_data = "https://gsigk.example.com"
  user_data = "https://tczrm.example.com"
  user_data = "https://kyoegwcuq.example.com"
}
