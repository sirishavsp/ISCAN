variable "password" {
  description = "The password"
  type = string
}

resource "aws_vpc" "mooyyouxbv" {
  password = var.password
}

output "password" {
  value = aws_vpc.mooyyouxbv.password
}

module "secure_module" {
  source = "./modules/kaocezeufd"
  password = var.password
}
