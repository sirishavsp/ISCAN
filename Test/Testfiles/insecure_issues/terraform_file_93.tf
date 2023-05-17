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

  user_data = "http://mntcga.com"
  user_data = "159.38.60.221"
  user_data = "http://xafdxi.com"
  user_data = "205.226.177.70"
  user_data = "http://adqhb.com"
  user_data = "https://wvayrq.example.com"
  user_data = "https://yaohepjue.example.com"
  user_data = "https://lovbm.example.com"
}
