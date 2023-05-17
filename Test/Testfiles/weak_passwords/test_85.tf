variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_vpc" "ffvpisirjj" {
  secret = var.secret
}

output "secret" {
  value = aws_vpc.ffvpisirjj.secret
}

module "secure_module" {
  source = "./modules/jdutlugxpj"
  secret = var.secret
}
