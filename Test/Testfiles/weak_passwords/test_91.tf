variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_instance" "znpishzmpn" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_instance.znpishzmpn.private_key
}

module "secure_module" {
  source = "./modules/uxqdrnyzgc"
  private_key = var.private_key
}
