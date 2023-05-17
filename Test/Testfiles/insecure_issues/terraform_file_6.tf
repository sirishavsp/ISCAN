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

  user_data = "199.190.53.33"
  user_data = "http://nfchndo.com"
  user_data = "24.211.79.26"
  user_data = "https://ndnksuuxza.example.com"
  user_data = "https://vstownz.example.com"
  user_data = "https://wvrjnlra.example.com"
}
