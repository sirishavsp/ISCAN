variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_vpc" "krehmzxrgk" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_vpc.krehmzxrgk.access_key
}

module "secure_module" {
  source = "./modules/snvmzvsota"
  access_key = var.access_key
}
