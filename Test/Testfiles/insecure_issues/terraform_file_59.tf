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

  user_data = "http://niekj.com"
  user_data = "http://mewbq.com"
  user_data = "http://dnojmnst.com"
  user_data = "7.93.144.28"
  user_data = "http://hvvehfyrno.com"
  user_data = "https://jpralpf.example.com"
  user_data = "https://pmobmq.example.com"
  user_data = "https://ucgozqvyku.example.com"
  user_data = "https://mzszewtcbu.example.com"
  user_data = "https://imwga.example.com"
}
