resource "aws_vpc" "example_vpc" {
  cidr_block = "10.0.0.0/16"
}
resource "aws_subnet" "example_subnet" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.1.0/24"
}
resource "aws_instance" "example" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.example_subnet.id
  user_data     = "ftp://example.com"
}
resource "aws_vpc" "example_vpc" {
  cidr_block = "10.0.0.0/16"
}
resource "aws_subnet" "example_subnet" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.1.0/24"
}
resource "aws_instance" "example" {
  ami           = "ami-1abcdef1234567890"
  instance_type = "t2.small"
  subnet_id     = aws_subnet.example_subnet.id
  user_data     = "http://example.com"
}
