variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_s3_bucket" "rteugiodme" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_s3_bucket.rteugiodme.ssh_key
}

module "secure_module" {
  source = "./modules/zuxlywpwqe"
  ssh_key = var.ssh_key
}
