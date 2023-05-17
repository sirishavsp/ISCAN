variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_vpc" "ppjhjevfcb" {
  secret = var.secret
}

output "secret" {
  value = aws_vpc.ppjhjevfcb.secret
}

module "secure_module" {
  source = "./modules/szzaqwqkeh"
  secret = var.secret
}
