variable "secret_key" {
  description = "The secret_key"
  type = string
}

resource "aws_vpc" "adgipbfytw" {
  secret_key = var.secret_key
}

output "secret_key" {
  value = aws_vpc.adgipbfytw.secret_key
}

module "secure_module" {
  source = "./modules/rvxrfuupqr"
  secret_key = var.secret_key
}
