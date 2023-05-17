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

  user_data = "http://tuisf.com"
  user_data = "http://ujwcqvl.com"
  user_data = "144.228.56.208"
  user_data = "92.94.200.221"
  user_data = "http://aaslzrnac.com"
  user_data = "https://rkslgkm.example.com"
  user_data = "https://mvcdd.example.com"
  user_data = "https://fchsxzaiw.example.com"
}
