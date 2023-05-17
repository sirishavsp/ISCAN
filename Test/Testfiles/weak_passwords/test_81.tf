variable "password" {
  description = "The password"
  type = string
}

resource "aws_vpc" "awptswgwbo" {
  password = var.password
}

output "password" {
  value = aws_vpc.awptswgwbo.password
}

module "secure_module" {
  source = "./modules/xhohbparbg"
  password = var.password
}
