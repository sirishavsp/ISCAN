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

  user_data = "129.38.168.196"
  user_data = "165.170.77.166"
  user_data = "198.163.205.184"
  user_data = "189.51.59.134"
  user_data = "67.11.189.116"
  user_data = "https://ovzisnuxza.example.com"
  user_data = "https://twtdhohrgc.example.com"
  user_data = "https://tepmisuyh.example.com"
}
