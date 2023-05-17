variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_instance" "hbbgigoaef" {
  secret = var.secret
}

output "secret" {
  value = aws_instance.hbbgigoaef.secret
}

module "secure_module" {
  source = "./modules/lqsuelvhjs"
  secret = var.secret
}
