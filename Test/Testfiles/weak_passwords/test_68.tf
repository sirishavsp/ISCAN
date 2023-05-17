variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_instance" "ankyjwnlqj" {
  secret = var.secret
}

output "secret" {
  value = aws_instance.ankyjwnlqj.secret
}

module "secure_module" {
  source = "./modules/stkkcakjuh"
  secret = var.secret
}
