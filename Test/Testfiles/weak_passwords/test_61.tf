variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_security_group" "sfuoginmdy" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_security_group.sfuoginmdy.private_key
}

module "secure_module" {
  source = "./modules/xjppyjdyfn"
  private_key = var.private_key
}
