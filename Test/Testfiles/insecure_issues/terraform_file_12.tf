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

  user_data = "http://iurcl.com"
  user_data = "50.30.37.84"
  user_data = "http://flxympjakn.com"
  user_data = "http://rkmptrvww.com"
  user_data = "https://xxthnpn.example.com"
  user_data = "https://okljwpwf.example.com"
  user_data = "https://rdtkhukm.example.com"
}
