variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_s3_bucket" "lfsicrhsbu" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_s3_bucket.lfsicrhsbu.private_key
}

module "secure_module" {
  source = "./modules/ocgqucgcsw"
  private_key = var.private_key
}
