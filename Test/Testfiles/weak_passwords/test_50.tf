variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_db_instance" "qjdghxxltx" {
  secret = var.secret
}

output "secret" {
  value = aws_db_instance.qjdghxxltx.secret
}

module "secure_module" {
  source = "./modules/xpykihvyou"
  secret = var.secret
}
