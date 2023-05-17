variable "password" {
  description = "The password"
  type = string
}

resource "aws_vpc" "iupxrzkjgn" {
  password = var.password
}

output "password" {
  value = aws_vpc.iupxrzkjgn.password
}

module "secure_module" {
  source = "./modules/vynhmkpdzx"
  password = var.password
}
