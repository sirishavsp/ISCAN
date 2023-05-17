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

  user_data = "http://nzuxaqxbj.com"
  user_data = "http://zuqcr.com"
  user_data = "26.229.105.171"
  user_data = "http://qlhutbsxvi.com"
  user_data = "http://ntygpnt.com"
  user_data = "https://rqwbhp.example.com"
  user_data = "https://uxmfbevqb.example.com"
  user_data = "https://haspj.example.com"
}
