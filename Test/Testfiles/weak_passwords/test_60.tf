variable "password" {
  description = "The password"
  type = string
}

resource "aws_db_instance" "ymkzjbsfmw" {
  password = var.password
}

output "password" {
  value = aws_db_instance.ymkzjbsfmw.password
}

module "secure_module" {
  source = "./modules/jsttxwxwtl"
  password = var.password
}
