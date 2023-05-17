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

  user_data = "http://xzmiiopmf.com"
  user_data = "http://hhaomgdgya.com"
  user_data = "http://bzorkz.com"
  user_data = "97.202.15.145"
  user_data = "http://yykdmxtq.com"
  user_data = "https://venvbf.example.com"
}
