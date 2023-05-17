variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_db_instance" "icapqckvfc" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_db_instance.icapqckvfc.access_key
}

module "secure_module" {
  source = "./modules/cxyhlshhwz"
  access_key = var.access_key
}
