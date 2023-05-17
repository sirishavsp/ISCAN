variable "secret_key" {
  description = "The secret_key"
  type = string
}

resource "aws_security_group" "gpohrscamg" {
  secret_key = var.secret_key
}

output "secret_key" {
  value = aws_security_group.gpohrscamg.secret_key
}

module "secure_module" {
  source = "./modules/qdqcdgjawq"
  secret_key = var.secret_key
}
