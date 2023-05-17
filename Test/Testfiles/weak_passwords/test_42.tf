variable "secret" {
  description = "The secret"
  type = string
}

resource "aws_s3_bucket" "ddnscylwam" {
  secret = var.secret
}

output "secret" {
  value = aws_s3_bucket.ddnscylwam.secret
}

module "secure_module" {
  source = "./modules/fjeavtpwmc"
  secret = var.secret
}
