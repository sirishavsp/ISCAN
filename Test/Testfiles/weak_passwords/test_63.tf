variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_security_group" "gjnqjyyeca" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_security_group.gjnqjyyeca.access_key
}

module "secure_module" {
  source = "./modules/ptnfuhxdpb"
  access_key = var.access_key
}
