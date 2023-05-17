variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_s3_bucket" "nkmncjiegg" {
  secret = var.secret
}

output "secret" {
  value = aws_s3_bucket.nkmncjiegg.secret
}

module "secure_module" {
  source = "./modules/srjejsccor"
  secret = var.secret
}
