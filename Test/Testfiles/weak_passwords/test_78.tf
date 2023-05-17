variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_vpc" "fdybzcfior" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_vpc.fdybzcfior.access_key
}

module "secure_module" {
  source = "./modules/bxwkhztess"
  access_key = var.access_key
}
