variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_instance" "hpfowrohmx" {
  secret = var.secret
}

output "secret" {
  value = aws_instance.hpfowrohmx.secret
}

module "secure_module" {
  source = "./modules/xkumkzumti"
  secret = var.secret
}
