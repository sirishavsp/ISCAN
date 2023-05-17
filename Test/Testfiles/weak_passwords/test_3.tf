variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_s3_bucket" "ssrpecauuv" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_s3_bucket.ssrpecauuv.ssh_key
}

module "secure_module" {
  source = "./modules/lxjemlomjc"
  ssh_key = var.ssh_key
}
