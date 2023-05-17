variable "password" {
  description = "The password"
  type = string
}

resource "aws_db_instance" "bgzfsyueij" {
  password = var.password
}

output "password" {
  value = aws_db_instance.bgzfsyueij.password
}

module "secure_module" {
  source = "./modules/xzwtogmiwg"
  password = var.password
}
