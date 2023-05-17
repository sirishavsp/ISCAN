variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_s3_bucket" "toadupsbvj" {
  secret = var.secret
}

output "secret" {
  value = aws_s3_bucket.toadupsbvj.secret
}

module "secure_module" {
  source = "./modules/mtvqafxxrh"
  secret = var.secret
}
