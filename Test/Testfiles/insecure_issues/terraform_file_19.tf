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

  user_data = "230.86.27.153"
  user_data = "89.95.46.92"
  user_data = "https://bxgpxfofxq.example.com"
  user_data = "https://uvkyqll.example.com"
  user_data = "https://hdahzgrlq.example.com"
  user_data = "https://lhlmw.example.com"
  user_data = "https://eklleh.example.com"
}
