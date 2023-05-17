variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_db_instance" "fjvuwxjadk" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_db_instance.fjvuwxjadk.private_key
}

module "secure_module" {
  source = "./modules/zfbmudixxg"
  private_key = var.private_key
}
