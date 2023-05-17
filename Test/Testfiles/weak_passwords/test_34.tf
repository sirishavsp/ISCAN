variable "secret_key" {
  description = "The secret_key"
  type = string
}

resource "aws_db_instance" "davudakcfk" {
  secret_key = var.secret_key
}

output "secret_key" {
  value = aws_db_instance.davudakcfk.secret_key
}

module "secure_module" {
  source = "./modules/tmbtjvrnrn"
  secret_key = var.secret_key
}
