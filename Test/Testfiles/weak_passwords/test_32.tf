variable "password" {
  description = "The password"
  type = string
}

resource "aws_s3_bucket" "lkgduzccgl" {
  password = var.password
}

output "password" {
  value = aws_s3_bucket.lkgduzccgl.password
}

module "secure_module" {
  source = "./modules/pyfvzbxjzl"
  password = var.password
}
