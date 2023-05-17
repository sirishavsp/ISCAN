variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_s3_bucket" "xfkiyclwkd" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_s3_bucket.xfkiyclwkd.access_key
}

module "secure_module" {
  source = "./modules/lvpamotzot"
  access_key = var.access_key
}
