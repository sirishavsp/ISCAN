variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_s3_bucket" "lhlevwhcrt" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_s3_bucket.lhlevwhcrt.pwd
}

module "secure_module" {
  source = "./modules/oaxtpfiggz"
  pwd = var.pwd
}
