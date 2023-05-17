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

  user_data = "83.34.133.163"
  user_data = "125.151.216.244"
  user_data = "249.146.173.31"
  user_data = "http://hfvhvtpz.com"
  user_data = "https://cozjtka.example.com"
  user_data = "https://mfbmqqe.example.com"
  user_data = "https://fxzxzu.example.com"
  user_data = "https://qleqqi.example.com"
  user_data = "https://aulbkbevj.example.com"
}
