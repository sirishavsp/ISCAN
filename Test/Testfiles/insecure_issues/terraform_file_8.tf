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

  user_data = "http://tylnnpcvor.com"
  user_data = "200.218.190.7"
  user_data = "http://osjpytqhs.com"
  user_data = "https://evuloarh.example.com"
  user_data = "https://mjebqmgiu.example.com"
  user_data = "https://pqrre.example.com"
  user_data = "https://wmkpybvlp.example.com"
}
