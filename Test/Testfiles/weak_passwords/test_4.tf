variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_db_instance" "ztgplkcdhp" {
  secret = var.secret
}

output "secret" {
  value = aws_db_instance.ztgplkcdhp.secret
}

module "secure_module" {
  source = "./modules/gmkztuwxno"
  secret = var.secret
}
