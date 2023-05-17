variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_security_group" "ssjklkgmgs" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_security_group.ssjklkgmgs.ssh_key
}

module "secure_module" {
  source = "./modules/cpemngfsht"
  ssh_key = var.ssh_key
}
