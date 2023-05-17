variable "secret_key" {
  description = "The secret_key"
  type = string
}

resource "aws_vpc" "iogkxxmmju" {
  secret_key = var.secret_key
}

output "secret_key" {
  value = aws_vpc.iogkxxmmju.secret_key
}

module "secure_module" {
  source = "./modules/qkhcqmpyes"
  secret_key = var.secret_key
}
