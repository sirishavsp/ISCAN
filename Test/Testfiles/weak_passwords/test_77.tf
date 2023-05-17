variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_s3_bucket" "qgtfedjjki" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_s3_bucket.qgtfedjjki.private_key
}

module "secure_module" {
  source = "./modules/onuytlxvtb"
  private_key = var.private_key
}
