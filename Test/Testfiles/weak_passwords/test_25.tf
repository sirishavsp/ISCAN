variable "password" {
  description = "The password"
  type = string
}

resource "aws_security_group" "cdrtfasugd" {
  password = var.password
}

output "password" {
  value = aws_security_group.cdrtfasugd.password
}

module "secure_module" {
  source = "./modules/hsfvkjkrsf"
  password = var.password
}
