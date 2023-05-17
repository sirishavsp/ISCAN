variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_vpc" "wsoafzsybo" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_vpc.wsoafzsybo.private_key
}

module "secure_module" {
  source = "./modules/lljrrtfjgy"
  private_key = var.private_key
}
