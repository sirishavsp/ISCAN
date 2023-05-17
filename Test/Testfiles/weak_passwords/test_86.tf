variable "password" {
  description = "The password"
  type = string
}

resource "aws_security_group" "phsbthcotb" {
  password = var.password
}

output "password" {
  value = aws_security_group.phsbthcotb.password
}

module "secure_module" {
  source = "./modules/zrvzhnyjfu"
  password = var.password
}
