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

  user_data = "http://wasnystr.com"
  user_data = "203.20.70.115"
  user_data = "http://lhmdjnd.com"
  user_data = "https://hsgrujaqu.example.com"
  user_data = "https://tgkdnavdad.example.com"
  user_data = "https://lyszcxe.example.com"
  user_data = "https://lvrnqroo.example.com"
}
