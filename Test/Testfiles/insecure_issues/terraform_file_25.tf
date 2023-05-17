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

  user_data = "119.80.39.38"
  user_data = "https://yayblmnz.example.com"
  user_data = "https://pjcvarczb.example.com"
  user_data = "https://ftjhqlgwaz.example.com"
}
