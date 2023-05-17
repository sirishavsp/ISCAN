variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_vpc" "rddknxjtyx" {
  secret = var.secret
}

output "secret" {
  value = aws_vpc.rddknxjtyx.secret
}

module "secure_module" {
  source = "./modules/ofvltwssnp"
  secret = var.secret
}
