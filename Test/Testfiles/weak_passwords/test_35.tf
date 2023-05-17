variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_db_instance" "nzcyjsifrb" {
  secret = var.secret
}

output "secret" {
  value = aws_db_instance.nzcyjsifrb.secret
}

module "secure_module" {
  source = "./modules/jdglzuvtkt"
  secret = var.secret
}
