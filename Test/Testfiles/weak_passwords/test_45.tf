variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_s3_bucket" "hcqaecczba" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_s3_bucket.hcqaecczba.private_key
}

module "secure_module" {
  source = "./modules/nydxgmgxfu"
  private_key = var.private_key
}
