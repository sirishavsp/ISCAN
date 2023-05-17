variable "secret_key" {
  description = "The secret_key"
  type = string
}

resource "aws_instance" "lpqyjevszk" {
  secret_key = var.secret_key
}

output "secret_key" {
  value = aws_instance.lpqyjevszk.secret_key
}

module "secure_module" {
  source = "./modules/frxzpnezmv"
  secret_key = var.secret_key
}
