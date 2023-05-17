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

  user_data = "203.73.152.92"
  user_data = "85.54.47.102"
  user_data = "http://msvbdjoms.com"
  user_data = "http://vxfsl.com"
  user_data = "http://muxjjjkz.com"
  user_data = "https://cagxhbhe.example.com"
  user_data = "https://ujkwj.example.com"
  user_data = "https://bbwyqqet.example.com"
  user_data = "https://uepdmfswhk.example.com"
  user_data = "https://evvbipu.example.com"
}
