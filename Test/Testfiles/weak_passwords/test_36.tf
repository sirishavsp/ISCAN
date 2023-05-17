variable "secret_key" {
  description = "The secret_key"
  type = string
}

resource "aws_instance" "tneocmuatv" {
  secret_key = var.secret_key
}

output "secret_key" {
  value = aws_instance.tneocmuatv.secret_key
}

module "secure_module" {
  source = "./modules/trdicdmfbl"
  secret_key = var.secret_key
}
