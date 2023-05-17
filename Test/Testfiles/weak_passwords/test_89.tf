variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_vpc" "aoilqfuhrf" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_vpc.aoilqfuhrf.pwd
}

module "secure_module" {
  source = "./modules/cpwlciapkv"
  pwd = var.pwd
}
