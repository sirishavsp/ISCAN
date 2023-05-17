variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_vpc" "llxonpwyfa" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_vpc.llxonpwyfa.pwd
}

module "secure_module" {
  source = "./modules/phbxisvyxz"
  pwd = var.pwd
}
