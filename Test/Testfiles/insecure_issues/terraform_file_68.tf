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

  user_data = "243.11.74.42"
  user_data = "https://pbayftgkd.example.com"
  user_data = "https://negzjkcjf.example.com"
  user_data = "https://jvduofxo.example.com"
  user_data = "https://jwogsdplpr.example.com"
  user_data = "https://cexyev.example.com"
}
