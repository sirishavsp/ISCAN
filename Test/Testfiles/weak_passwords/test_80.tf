variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_security_group" "gqdktndywi" {
  secret = var.secret
}

output "secret" {
  value = aws_security_group.gqdktndywi.secret
}

module "secure_module" {
  source = "./modules/trczineqsr"
  secret = var.secret
}
