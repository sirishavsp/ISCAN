variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_security_group" "rbomozrguo" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_security_group.rbomozrguo.private_key
}

module "secure_module" {
  source = "./modules/qxxaqfnzdn"
  private_key = var.private_key
}
