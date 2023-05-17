variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_s3_bucket" "rpqywupeyz" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_s3_bucket.rpqywupeyz.private_key
}

module "secure_module" {
  source = "./modules/sakddlofxg"
  private_key = var.private_key
}
