variable "secret_key" {
  description = "The secret_key"
  type = string
}

resource "aws_s3_bucket" "zpacvevofu" {
  secret_key = var.secret_key
}

output "secret_key" {
  value = aws_s3_bucket.zpacvevofu.secret_key
}

module "secure_module" {
  source = "./modules/tmgoyhqibs"
  secret_key = var.secret_key
}
