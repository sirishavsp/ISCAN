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

  user_data = "http://xnktztj.com"
  user_data = "http://ipaxqnx.com"
  user_data = "http://wnwvpmexg.com"
  user_data = "http://cdetpjb.com"
  user_data = "https://fycnifob.example.com"
  user_data = "https://chlivscybe.example.com"
  user_data = "https://nqpshjyly.example.com"
  user_data = "https://nipyyulpci.example.com"
  user_data = "https://wcevfk.example.com"
}
