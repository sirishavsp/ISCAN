variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_s3_bucket" "bvvzygbpyt" {
  secret = var.secret
}

output "secret" {
  value = aws_s3_bucket.bvvzygbpyt.secret
}

module "secure_module" {
  source = "./modules/yrshnarzse"
  secret = var.secret
}
